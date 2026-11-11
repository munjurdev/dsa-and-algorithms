"""
Solution for: Maximum Average Subarray I
Day:      day-10
Track:    algorithms
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Compute the sum of the first `k` elements, then slide the window one slot
    at a time: add the entering element and subtract the leaving one, so each
    window sum costs O(1) instead of a fresh O(k) sum. Track the largest window
    sum and divide it by `k` exactly once at the end — dividing only at the
    return keeps every intermediate value an exact integer.

Time Complexity:  O(n)   # one pass: n - k slides, constant work each
Space Complexity: O(1)   # two sums and a couple of indices, no extra array
"""

from __future__ import annotations

import random


def find_max_average(nums: list[int], k: int) -> float:
    """Return the maximum average of any length-`k` contiguous subarray.

    Args:
        nums: non-empty list of integers; negatives and zeros are allowed.
        k: window length, `1 <= k <= len(nums)`.

    Returns:
        The largest `sum(nums[i:i + k]) / k` over all valid `i`, as a float.

    Raises:
        ValueError: if `k <= 0`, or if `k > len(nums)` so no window exists.
    """
    # --- Solution -------------------------------------------------------
    if k <= 0:
        raise ValueError("window length k must be positive")
    if k > len(nums):
        raise ValueError("window length k cannot exceed len(nums)")

    window_sum = sum(nums[:k])
    best_sum = window_sum
    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        if window_sum > best_sum:
            best_sum = window_sum
    return best_sum / k


def _brute_force_average(nums: list[int], k: int) -> float:
    """O(n·k) reference: sum every window from scratch."""
    best_sum = max(sum(nums[start : start + k]) for start in range(len(nums) - k + 1))
    return best_sum / k


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's example
    assert abs(find_max_average([1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-9

    # Degenerate sizes: k = 1 and k = n
    assert find_max_average([5], 1) == 5.0
    assert find_max_average([-1], 1) == -1.0
    assert find_max_average([1, 2, 3, 4], 4) == 2.5
    assert find_max_average([1, 2, 3, 4], 1) == 4.0

    # All negatives: the answer must be the least-bad window, not 0
    assert find_max_average([-5, -3, -8, -1], 2) == -4.0
    assert find_max_average([-10000], 1) == -10000.0

    # Zeros: a zero average is still an average
    assert find_max_average([0, 0, 0, 0, 0], 3) == 0.0
    assert find_max_average([0, 4, 0, 3, 2], 1) == 4.0

    # Best window can sit at the very start or the very end
    assert find_max_average([10, 0, 0, 0, 1], 2) == 5.0
    assert find_max_average([0, 0, 0, 1, 10], 2) == 5.5

    # Fractional averages and the returned type
    assert abs(find_max_average([1, 2], 2) - 1.5) < 1e-9
    assert abs(find_max_average([2, -1, 2, -1, 2], 3) - 1.0) < 1e-9
    assert isinstance(find_max_average([3], 1), float)

    # Invalid window lengths are rejected, not silently answered
    for bad_k in (0, -1, 5):
        try:
            find_max_average([1, 2, 3], bad_k)
        except ValueError:
            pass
        else:
            raise AssertionError(f"expected ValueError for k={bad_k}")

    # The caller's list is never mutated
    nums = [1, 12, -5, -6, 50, 3]
    assert abs(find_max_average(nums, 4) - 12.75) < 1e-9
    assert nums == [1, 12, -5, -6, 50, 3]

    # Exhaustive differential check on tiny arrays against the brute force
    for size in range(1, 7):
        for values in _tuples_of(range(-3, 4), size):
            nums = list(values)
            for k in range(1, size + 1):
                got = find_max_average(nums, k)
                want = _brute_force_average(nums, k)
                assert abs(got - want) < 1e-9, (nums, k, got, want)

    # Randomized check on longer arrays, negatives and zeros included
    rng = random.Random(20261111)
    for _ in range(500):
        size = rng.randint(1, 40)
        nums = [rng.randint(-10, 10) for _ in range(size)]
        k = rng.randint(1, size)
        got = find_max_average(nums, k)
        want = _brute_force_average(nums, k)
        assert abs(got - want) < 1e-9, (nums, k, got, want)

    print("All tests passed.")


def _tuples_of(values: range, size: int):
    """Yield every `size`-tuple drawn from `values` (order matters)."""
    if size == 0:
        yield ()
        return
    for head in values:
        for tail in _tuples_of(values, size - 1):
            yield (head, *tail)


if __name__ == "__main__":
    main()
