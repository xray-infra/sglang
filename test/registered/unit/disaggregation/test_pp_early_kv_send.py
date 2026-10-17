"""PP disagg prefill: each stage sends its KV once its final-chunk forward is done."""

import contextlib
import os
import unittest
from types import SimpleNamespace
from unittest.mock import Mock, patch

import torch

from sglang.srt.disaggregation.base import KVPoll
from sglang.srt.disaggregation.prefill import (
    PPEarlyKVSend,
    SchedulerDisaggregationPrefillMixin,
)
from sglang.srt.disaggregation.utils import TransferBackend
from sglang.test.ci.ci_register import register_cpu_ci
from sglang.test.test_utils import CustomTestCase

register_cpu_ci(est_time=2, suite="base-a-test-cpu")

M = SchedulerDisaggregationPrefillMixin
POLL = "sglang.srt.disaggregation.prefill.poll_and_all_reduce_attn_cp_tp_group"


def make_req(rid, **kw):
    values = dict(
        rid=rid,
        return_logprob=False,
        return_sampling_mask=False,
        grammar=None,
        bootstrap_host="prefill",
        finished_reason=None,
        to_finish=None,
        pending_bootstrap=True,
        pp_early_kv_send=False,
        output_ids=[],
        disagg_kv_sender=Mock(),
    )
    values.update(kw)
    return SimpleNamespace(**values)


def make_scheduler(last_rank):
    events = []

    def new_event():
        ev = Mock()
        events.append(ev)
        return ev

    s = SimpleNamespace(
        chunked_req=None,
        disagg_pp_early_kv_reqs=[],
        pp_group=SimpleNamespace(is_last_rank=last_rank),
        forward_stream_ctx=contextlib.nullcontext(),
        device_module=SimpleNamespace(Event=new_event, current_stream=Mock()),
        spec_algorithm=SimpleNamespace(is_eagle=lambda: True),
        attn_cp_cpu_group=None,
        attn_tp_cpu_group=None,
        send_kv_chunk=Mock(),
        events=events,
    )
    s.pp_early_kv_send_enabled = lambda: True
    s._pp_copy_early_kv_aux = lambda result: M._pp_copy_early_kv_aux(s, result)

    def handle_pending_bootstrap(req, poll, *, checkpoint=True):
        assert checkpoint is False
        req.pending_bootstrap = False
        return True

    s.handle_pending_bootstrap = Mock(side_effect=handle_pending_bootstrap)
    return s


def extend_batch(reqs):
    return SimpleNamespace(
        reqs=reqs, forward_mode=SimpleNamespace(is_extend=lambda: True)
    )


def last_rank_result():
    return SimpleNamespace(
        next_token_ids=torch.tensor([11, 22, 33]),
        next_draft_input=SimpleNamespace(
            topk_p=torch.rand(3, 4),
            topk_index=torch.arange(12).view(3, 4),
            hidden_states=torch.rand(3, 8),
            dsa_topk_indices=None,
        ),
    )


class TestRegister(CustomTestCase):
    def test_only_final_chunks_of_plain_requests_are_registered(self):
        s = make_scheduler(last_rank=False)
        final = make_req("final")
        chunked = make_req("chunked")
        logprob = make_req("logprob", return_logprob=True)
        s.chunked_req = chunked
        M.register_pp_early_kv_send(
            s, extend_batch([final, chunked, logprob]), SimpleNamespace()
        )
        self.assertEqual([e.req for e in s.disagg_pp_early_kv_reqs], [final])
        self.assertIsNone(s.disagg_pp_early_kv_reqs[0].aux)
        self.assertTrue(final.pp_early_kv_send)
        self.assertFalse(chunked.pp_early_kv_send)
        self.assertFalse(logprob.pp_early_kv_send)
        # Decode may allocate now, while later stages still compute.
        final.disagg_kv_sender.mark_prefill_complete.assert_called_once_with()
        chunked.disagg_kv_sender.mark_prefill_complete.assert_not_called()
        # The readiness event is recorded after the forward.
        s.events[0].record.assert_called_once()

    def test_last_stage_keeps_host_copies_of_its_rows(self):
        s = make_scheduler(last_rank=True)
        reqs = [make_req("a"), make_req("b", grammar=object()), make_req("c")]
        result = last_rank_result()
        M.register_pp_early_kv_send(s, extend_batch(reqs), result)
        a, c = s.disagg_pp_early_kv_reqs
        self.assertEqual((a.req.rid, c.req.rid), ("a", "c"))
        self.assertEqual(int(a.aux["next_token_ids"]), 11)
        self.assertEqual(int(c.aux["next_token_ids"]), 33)
        self.assertTrue(torch.equal(c.aux["topk_index"], torch.arange(8, 12)))
        self.assertTrue(
            torch.equal(c.aux["hidden_states"], result.next_draft_input.hidden_states[2])
        )
        self.assertNotIn("dsa_topk_indices", c.aux)

    def test_disabled_registers_nothing(self):
        s = make_scheduler(last_rank=False)
        s.pp_early_kv_send_enabled = lambda: False
        req = make_req("a")
        M.register_pp_early_kv_send(s, extend_batch([req]), SimpleNamespace())
        self.assertEqual(s.disagg_pp_early_kv_reqs, [])
        self.assertFalse(req.pp_early_kv_send)

    def test_enabled_only_for_supported_topology(self):
        base = SimpleNamespace(
            transfer_backend=TransferBackend.MOONCAKE,
            enable_staging=False,
            kv_checksum_computer=None,
            tree_cache=SimpleNamespace(),
        )
        parallel = SimpleNamespace(pp_size=8, attn_tp_size=1, attn_cp_size=1)
        disagg = SimpleNamespace(
            disaggregation_decode_allocation_policy="prefill_complete"
        )
        cases = [
            ({}, {}, "1", True),
            ({}, {}, "0", False),
            ({}, {"pp_size": 1}, "1", False),
            ({}, {"attn_tp_size": 2}, "1", False),
            ({"enable_staging": True}, {}, "1", False),
            ({"tree_cache": SimpleNamespace(linker=object())}, {}, "1", False),
        ]
        for sched_kw, par_kw, env, expected in cases:
            with self.subTest(sched=sched_kw, par=par_kw, env=env):
                s = SimpleNamespace(**{**vars(base), **sched_kw})
                p = SimpleNamespace(**{**vars(parallel), **par_kw})
                with patch(
                    "sglang.srt.disaggregation.prefill.get_parallel", return_value=p
                ), patch(
                    "sglang.srt.disaggregation.prefill.get_disagg", return_value=disagg
                ), patch.dict(
                    os.environ, {"SGLANG_DISAGGREGATION_PP_EARLY_KV_SEND": env}
                ):
                    self.assertEqual(M.pp_early_kv_send_enabled(s), expected)


class TestPoll(CustomTestCase):
    def poll(self, s, polls):
        with patch(POLL, return_value=polls):
            M.process_pp_early_kv_send(s)

    def test_earlier_stage_sends_kv_without_aux_once_destinations_arrive(self):
        s = make_scheduler(last_rank=False)
        req = make_req("a", pp_early_kv_send=True)
        ready = Mock()
        s.disagg_pp_early_kv_reqs = [PPEarlyKVSend(req, ready)]
        self.poll(s, [KVPoll.Bootstrapping])
        s.send_kv_chunk.assert_not_called()
        self.assertEqual(len(s.disagg_pp_early_kv_reqs), 1)

        self.poll(s, [KVPoll.WaitingForInput])
        s.send_kv_chunk.assert_called_once_with(req, last_chunk=True, skip_aux=True)
        # The transfer worker, not the scheduler, waits for the forward.
        self.assertIs(req.disagg_kv_sender._early_send_wait_event, ready)
        ready.query.assert_not_called()
        self.assertFalse(req.pending_bootstrap)
        self.assertEqual(s.disagg_pp_early_kv_reqs, [])

    def test_last_stage_waits_for_its_host_copies_then_sends_aux(self):
        s = make_scheduler(last_rank=True)
        req = make_req("a", pp_early_kv_send=True)
        result = last_rank_result()
        M.register_pp_early_kv_send(s, extend_batch([req]), result)
        ready = s.events[0]
        ready.query.return_value = False
        self.poll(s, [KVPoll.WaitingForInput])
        s.send_kv_chunk.assert_not_called()
        s.handle_pending_bootstrap.assert_not_called()
        self.assertTrue(req.pending_bootstrap)

        ready.query.return_value = True
        self.poll(s, [KVPoll.WaitingForInput])
        s.send_kv_chunk.assert_called_once_with(
            req, last_chunk=True, first_token_id=11
        )
        self.assertTrue(
            torch.equal(req.output_topk_p, result.next_draft_input.topk_p[0])
        )
        self.assertTrue(
            torch.equal(
                req.hidden_states_tensor, result.next_draft_input.hidden_states[0]
            )
        )
        self.assertIsNone(req.output_dsa_topk_indices)
        self.assertEqual(s.disagg_pp_early_kv_reqs, [])

    def test_after_the_batch_result_it_is_a_regular_send(self):
        s = make_scheduler(last_rank=True)
        req = make_req("a", pp_early_kv_send=True, output_ids=[11])
        ready = Mock()
        ready.query.return_value = False
        s.disagg_pp_early_kv_reqs = [
            PPEarlyKVSend(req, ready, {"next_token_ids": torch.tensor(11)})
        ]
        self.poll(s, [KVPoll.WaitingForInput])
        s.send_kv_chunk.assert_called_once_with(req, last_chunk=True)
        self.assertEqual(s.disagg_pp_early_kv_reqs, [])

    def test_finalized_retired_or_aborted_entries_are_dropped(self):
        from sglang.srt.managers.schedule_batch import FINISH_ABORT

        s = make_scheduler(last_rank=False)
        finalized = make_req("finalized", pending_bootstrap=False)
        aborted = make_req("aborted", to_finish=FINISH_ABORT("x"))
        waiting = make_req("waiting")
        s.disagg_pp_early_kv_reqs = [
            PPEarlyKVSend(r, Mock()) for r in (finalized, aborted, waiting)
        ]
        with patch(POLL, return_value=[KVPoll.Bootstrapping]) as poll:
            M.process_pp_early_kv_send(s)
        self.assertEqual(poll.call_args.args[0], [waiting.disagg_kv_sender])
        self.assertEqual([e.req for e in s.disagg_pp_early_kv_reqs], [waiting])
        s.send_kv_chunk.assert_not_called()


class TestBatchResultCheckpoint(CustomTestCase):
    def test_as_pending_never_publishes(self):
        cache = Mock()
        s = SimpleNamespace(tree_cache=cache)
        req = SimpleNamespace(pending_bootstrap=False, extend_end=4096)
        with patch(
            "sglang.srt.disaggregation.prefill.checkpoint_kv_cache"
        ) as checkpoint:
            M.checkpoint_disagg_prefill(s, req, as_pending=True)
            checkpoint.assert_not_called()
            M.checkpoint_disagg_prefill(s, req)
            checkpoint.assert_called_once_with(req, cache)

    def test_as_pending_matches_a_parked_request_on_write_through_cache(self):
        s = SimpleNamespace(tree_cache=Mock())
        req = SimpleNamespace(pending_bootstrap=False, extend_end=4096, prefix_len=0)
        with patch(
            "sglang.srt.disaggregation.prefill._uses_write_through_cache",
            return_value=True,
        ):
            M.checkpoint_disagg_prefill(s, req, as_pending=True)
        s.tree_cache.advance_unpublished_req.assert_called_once_with(req)
        self.assertEqual(req.prefix_len, 4096)


if __name__ == "__main__":
    unittest.main()
