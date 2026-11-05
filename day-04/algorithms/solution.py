"""
Solution for: Maximum Subarray (Kadane's algorithm)
Day:      day-04
Track:    algorithms
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Keep two registers seeded with the first element: `best_ending_here`, the
    maximum sum of a subarray ending at the current index, and `best`, the
    maximum seen anywhere so far. Each new value either extends the current
    run or restarts at itself — `max(value, best_ending_here + value)` — and
    the global answer is updated from that. Seeding from `nums[0]` instead of
    0 is what makes the all-negative case return the largest single element
    rather than the forbidden empty sum.

Time Complexity:  O(n)   # one pass, constant work per element
Space Complexity: O(1)   # two integers regardless of input size

Review Date:  2026-11-06 / 2026-11-12 / 2026-12-05
"""

from __future__ import annotations

import random


def max_subarray(nums: list[int]) -> int:
    """Return the largest sum of any non-empty contiguous subarray.

    Args:
        nums: array of integers; negatives and zeros allowed.

    Returns:
        The maximum sum over all slices `nums[i:j + 1]`.

    Raises:
        ValueError: if `nums` is empty (no non-empty subarray exists).
    """
    if not nums:
        raise ValueError("nums must contain at least one element")

    # --- Solution -------------------------------------------------------
    best_ending_here = nums[0]  # best run that must end at the current index
    best = nums[0]              # best run seen anywhere so far
    for value in nums[1:]:
        best_ending_here = max(value, best_ending_here + value)
        best = max(best, best_ending_here)
    return best


def _brute_force(nums: list[int]) -> int:
    """O(n^2) reference implementation, used only to differential-test above."""
    best = nums[0]
    for left in range(len(nums)):
        running = 0
        for right in range(left, len(nums)):
            running += nums[right]
            best = max(best, running)
    return best


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # Typical case from the statement
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([5, 4, -1, 7, 8]) == 23

    # Edge cases: single element, all negative, zeros
    assert max_subarray([1]) == 1
    assert max_subarray([5]) == 5
    assert max_subarray([-1]) == -1
    assert max_subarray([-3, -1, -2]) == -1    # all negative: best single value
    assert max_subarray([-2, -1]) == -1        # never return 0 here
    assert max_subarray([0, -1]) == 0          # a zero run is still a subarray
    assert max_subarray([0, 0, 0]) == 0

    # Empty input is rejected rather than answered with a sentinel
    try:
        max_subarray([])
    except ValueError:
        pass
    else:
        raise AssertionError("empty input should raise")

    # Differential check over every slice: Kadane == brute force
    rng = random.Random(20261105)
    for _ in range(300):
        size = rng.randint(1, 30)
        nums = [rng.randint(-10, 10) for _ in range(size)]
        assert max_subarray(nums) == _brute_force(nums), nums

    print("All tests passed.")


if __name__ == "__main__":
    main()
