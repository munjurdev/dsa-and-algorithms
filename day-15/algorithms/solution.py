"""
Solution for: Sliding Window Maximum
Day:      day-15
Track:    algorithms
Difficulty: Hard

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Sweep the array once with a deque of indices whose values are strictly
    decreasing from front to back, so the front index is always the maximum of
    the current window. For each new element, pop smaller-or-equal indices from
    the back (they can never be a maximum again while this element is in the
    window), append the new index, drop the front index if it has fallen out of
    the window, and record the front once the window is full. Every index is
    appended once and popped once, so the whole scan is O(n) rather than the
    O(n*k) of re-scanning each window.

Time Complexity:  O(n)  # each index enters and leaves the deque at most once
Space Complexity: O(k)  # the deque holds at most one window's worth of indices

Review Date:  2026-11-22 (1 day) · 2026-11-28 (7 days) · 2026-12-21 (30 days)
"""

from __future__ import annotations

import random
from collections import deque


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    """Return the maximum of every length-`k` window of `nums`.

    Args:
        nums: the array to scan; may be empty depending on the caller.
        k: window width, `1 <= k <= len(nums)` as the platform guarantees.

    Returns:
        A list of length `len(nums) - k + 1`, one maximum per window; `[]` when
        `nums` is empty or shorter than `k`.

    Raises:
        ValueError: if `k <= 0`.
    """
    if k <= 0:
        raise ValueError("window size must be positive")
    if k > len(nums):
        return []

    # --- Solution -------------------------------------------------------
    candidates: deque[int] = deque()  # indices, values strictly decreasing
    result: list[int] = []

    for index, value in enumerate(nums):
        # Smaller-or-equal values can never be a window maximum again.
        while candidates and nums[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(index)

        window_start = index - k + 1
        # Evict the front before reading it: it may have left the window.
        if candidates[0] < window_start:
            candidates.popleft()

        if window_start >= 0:
            result.append(nums[candidates[0]])

    return result


def _max_sliding_window_brute(nums: list[int], k: int) -> list[int]:
    """O(n*k) reference: take the maximum of every window directly."""
    return [max(nums[start : start + k]) for start in range(len(nums) - k + 1)]


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # --- Statement examples ---------------------------------------------
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert max_sliding_window([1], 1) == [1]
    assert max_sliding_window([1, -1], 1) == [1, -1]
    assert max_sliding_window([9, 11], 2) == [11]
    assert max_sliding_window([4, -2], 2) == [4]
    assert max_sliding_window([-7, -8, 7, 5, 7, 1, 6, 0], 4) == [7, 7, 7, 7, 7]

    # --- Edge cases: empty, window wider than the array, invalid k --------
    assert max_sliding_window([], 1) == []
    assert max_sliding_window([1, 2], 3) == []
    try:
        max_sliding_window([1, 2], 0)
    except ValueError:
        pass
    else:  # pragma: no cover - only runs if the guard is missing
        raise AssertionError("k = 0 must be rejected")

    # --- Windows that start at 0 and end at the last index ----------------
    assert max_sliding_window([1, 2, 3, 4, 5], 5) == [5]      # k = n
    assert max_sliding_window([5, 4, 3, 2, 1], 5) == [5]
    assert max_sliding_window([2, 2, 2, 2], 2) == [2, 2, 2]   # all equal

    # --- Randomized differential check against the brute force -----------
    rng = random.Random(20261121)
    for _ in range(500):
        size = rng.randint(0, 60)
        numbers = [rng.randint(-50, 50) for _ in range(size)]
        if not numbers:
            assert max_sliding_window(numbers, 1) == []
            continue
        width = rng.randint(1, size)
        assert max_sliding_window(numbers, width) == _max_sliding_window_brute(
            numbers, width
        ), (numbers, width)

    # --- Full-size shapes: the two inputs that stress each deque end ------
    # Increasing input pops the back on every step; decreasing input expires
    # the front on every step. Both are n = 100,000, the platform's limit.
    size = 100_000
    width = 1_000
    increasing = list(range(1, size + 1))
    assert max_sliding_window(increasing, width) == list(
        range(width, size + 1)
    )
    decreasing = list(range(size, 0, -1))
    assert max_sliding_window(decreasing, width) == [
        size - start for start in range(size - width + 1)
    ]

    print("All tests passed.")


if __name__ == "__main__":
    main()
