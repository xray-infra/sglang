from __future__ import annotations

from typing import Any, Dict, List, Mapping, Optional, final

from sglang.srt.entrypoints.openai.protocol import (
    CacheCreationTokenDetails,
    PromptTokensDetails,
    UsageInfo,
)


@final
class UsageProcessor:
    """Stateless helpers that turn raw token counts into a UsageInfo."""

    @staticmethod
    def _details_if_cached(
        count: int,
        cache_write_tokens: Optional[int] = None,
        cache_write_tokens_by_ttl: Optional[Dict[int, int]] = None,
    ) -> Optional[PromptTokensDetails]:
        """Return details when read or write cache accounting is available."""
        if count <= 0 and cache_write_tokens is None:
            return None
        cache_creation_token_details = None
        if cache_write_tokens_by_ttl is not None:
            cache_creation_token_details = CacheCreationTokenDetails(
                ephemeral_5m_input_tokens=cache_write_tokens_by_ttl.get(300, 0),
                ephemeral_1h_input_tokens=cache_write_tokens_by_ttl.get(3600, 0),
            )
        return PromptTokensDetails(
            cached_tokens=count,
            cache_write_tokens=cache_write_tokens,
            cache_creation_token_details=cache_creation_token_details,
        )

    @staticmethod
    def _known_total(counts: List[Optional[int]]) -> Optional[int]:
        """Sum counters only when every request reported the counter."""
        if any(count is None for count in counts):
            return None
        return sum(count for count in counts if count is not None)

    @staticmethod
    def _response_write_total(
        responses: List[Dict[str, Any]], n_choices: int, field_name: str
    ) -> Optional[int]:
        per_prompt_writes = []
        for start in range(0, len(responses), n_choices):
            choice_writes = [
                response["meta_info"].get(field_name)
                for response in responses[start : start + n_choices]
            ]
            if any(count is None for count in choice_writes):
                per_prompt_writes.append(None)
            else:
                per_prompt_writes.append(
                    max(count for count in choice_writes if count is not None)
                )
        return UsageProcessor._known_total(per_prompt_writes)

    @staticmethod
    def _stream_write_total(
        values: Mapping[int, Optional[int]],
        prompt_indices: List[int],
        n_choices: int,
    ) -> Optional[int]:
        per_prompt_writes = []
        for prompt_idx in prompt_indices:
            choice_writes = [
                values.get(idx) for idx in range(prompt_idx, prompt_idx + n_choices)
            ]
            if any(count is None for count in choice_writes):
                per_prompt_writes.append(None)
            else:
                per_prompt_writes.append(
                    max(count for count in choice_writes if count is not None)
                )
        return UsageProcessor._known_total(per_prompt_writes)

    @staticmethod
    def _response_ttl_totals(
        responses: List[Dict[str, Any]], n_choices: int
    ) -> Optional[Dict[int, int]]:
        total_by_ttl: Dict[int, int] = {}
        for start in range(0, len(responses), n_choices):
            choice_details = [
                response["meta_info"].get("cache_write_tokens_by_ttl")
                for response in responses[start : start + n_choices]
            ]
            if any(details is None for details in choice_details):
                return None
            known_choice_details = [
                details for details in choice_details if details is not None
            ]
            ttl_values = {
                ttl_seconds
                for details in known_choice_details
                for ttl_seconds in details
            }
            for ttl_seconds in ttl_values:
                total_by_ttl[ttl_seconds] = total_by_ttl.get(ttl_seconds, 0) + max(
                    details.get(ttl_seconds, 0) for details in known_choice_details
                )
        return total_by_ttl

    @staticmethod
    def _stream_ttl_totals(
        values: Mapping[int, Optional[Dict[int, int]]],
        prompt_indices: List[int],
        n_choices: int,
    ) -> Optional[Dict[int, int]]:
        total_by_ttl: Dict[int, int] = {}
        for prompt_idx in prompt_indices:
            choice_details = [
                values.get(idx) for idx in range(prompt_idx, prompt_idx + n_choices)
            ]
            if any(details is None for details in choice_details):
                return None
            known_choice_details = [
                details for details in choice_details if details is not None
            ]
            ttl_values = {
                ttl_seconds
                for details in known_choice_details
                for ttl_seconds in details
            }
            for ttl_seconds in ttl_values:
                total_by_ttl[ttl_seconds] = total_by_ttl.get(ttl_seconds, 0) + max(
                    details.get(ttl_seconds, 0) for details in known_choice_details
                )
        return total_by_ttl

    @staticmethod
    def calculate_response_usage(
        responses: List[Dict[str, Any]],
        n_choices: int = 1,
        enable_cache_report: bool = False,
        image_tokens: int = 0,
        audio_tokens: int = 0,
        video_tokens: int = 0,
    ) -> UsageInfo:
        completion_tokens = sum(
            r["meta_info"].get("completion_tokens", 0) for r in responses
        )
        prompt_responses = responses[::n_choices]
        prompt_tokens = sum(
            response["meta_info"].get("prompt_tokens", 0)
            for response in prompt_responses
        )

        # some API don't have reasoning_tokens semantics
        reasoning_tokens = sum(
            r["meta_info"].get("reasoning_tokens", 0) for r in responses
        )

        cached_details = None
        if enable_cache_report:
            cached_total = sum(
                response["meta_info"].get("cached_tokens", 0)
                for response in prompt_responses
            )
            cache_write_total = UsageProcessor._response_write_total(
                responses, n_choices, "cache_write_tokens"
            )
            cache_write_tokens_by_ttl = UsageProcessor._response_ttl_totals(
                responses, n_choices
            )
            cached_details = UsageProcessor._details_if_cached(
                cached_total,
                cache_write_total,
                cache_write_tokens_by_ttl,
            )

        return UsageProcessor.calculate_token_usage(
            prompt_tokens=prompt_tokens,
            reasoning_tokens=reasoning_tokens,
            completion_tokens=completion_tokens,
            cached_tokens=cached_details,
            image_tokens=image_tokens,
            audio_tokens=audio_tokens,
            video_tokens=video_tokens,
        )

    @staticmethod
    def calculate_streaming_usage(
        prompt_tokens: Mapping[int, int],
        reasoning_tokens: Mapping[int, int],
        completion_tokens: Mapping[int, int],
        cached_tokens: Mapping[int, int],
        cache_write_tokens: Mapping[int, Optional[int]],
        cache_write_tokens_by_ttl: Mapping[int, Optional[Dict[int, int]]],
        n_choices: int,
        enable_cache_report: bool = False,
        image_tokens: int = 0,
        audio_tokens: int = 0,
        video_tokens: int = 0,
    ) -> UsageInfo:
        # index % n_choices == 0 marks the first choice of a prompt
        prompt_indices = [idx for idx in prompt_tokens if idx % n_choices == 0]
        total_prompt_tokens = sum(prompt_tokens[idx] for idx in prompt_indices)
        total_reasoning_tokens = sum(reasoning_tokens.values())
        total_completion_tokens = sum(completion_tokens.values())

        cached_details = None
        if enable_cache_report:
            cached_total = sum(cached_tokens.get(idx, 0) for idx in prompt_indices)
            cache_write_total = UsageProcessor._stream_write_total(
                cache_write_tokens, prompt_indices, n_choices
            )
            ttl_totals = UsageProcessor._stream_ttl_totals(
                cache_write_tokens_by_ttl, prompt_indices, n_choices
            )
            cached_details = UsageProcessor._details_if_cached(
                cached_total,
                cache_write_total,
                ttl_totals,
            )

        return UsageProcessor.calculate_token_usage(
            prompt_tokens=total_prompt_tokens,
            reasoning_tokens=total_reasoning_tokens,
            completion_tokens=total_completion_tokens,
            cached_tokens=cached_details,
            image_tokens=image_tokens,
            audio_tokens=audio_tokens,
            video_tokens=video_tokens,
        )

    @staticmethod
    def calculate_token_usage(
        prompt_tokens: int,
        completion_tokens: int,
        reasoning_tokens: Optional[int] = 0,
        cached_tokens: Optional[PromptTokensDetails] = None,
        image_tokens: int = 0,
        audio_tokens: int = 0,
        video_tokens: int = 0,
    ) -> UsageInfo:
        """Calculate token usage information"""
        # `cached_tokens` is already a PromptTokensDetails (or None) carrying the
        # cached count. Attach multimodal counts to the same object, creating one
        # only when there is something to report so plain-text requests keep
        # prompt_tokens_details=None (backward compatible).
        details = cached_tokens
        if image_tokens or audio_tokens or video_tokens:
            if details is None:
                details = PromptTokensDetails()
            if image_tokens:
                details.image_tokens = image_tokens
            if audio_tokens:
                details.audio_tokens = audio_tokens
            if video_tokens:
                details.video_tokens = video_tokens

        return UsageInfo(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=prompt_tokens + completion_tokens,
            prompt_tokens_details=details,
            reasoning_tokens=reasoning_tokens,
        )
