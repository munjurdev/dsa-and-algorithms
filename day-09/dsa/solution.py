"""
Solution for: Subarray Sum Equals K
Day:      day-09
Track:    dsa
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    A subarray `nums[i:j]` sums to `k` exactly when
    `prefix[j] - prefix[i] == k`, i.e. `prefix[i] == prefix[j] - k`. Scan once,
    keeping a map from each prefix value to how many times it has occurred.
    The empty prefix counts as one occurrence, so a subarray starting at index
    0 is found. At each new prefix value, add the count of
    `prefix - k` to the answer, then record the current prefix.

Time Complexity:  O(n)   # one pass; each map lookup/update is O(1) average
Space Complexity: O(n)   # at most n + 1 distinct prefix values stored
"""

from __future__ import annotations

import random


def subarray_sum(nums: list[int], k: int) -> int:
    """Count the contiguous subarrays of `nums` whose sum equals `k`.

    Args:
        nums: array of integers; negatives are allowed, so a window cannot be
            used (the sum is not monotone in the window bounds).
        k: target sum.

    Returns:
        The number of index pairs `i <= j` with `sum(nums[i:j + 1]) == k`.
        An empty array returns `0`.
    """
    # --- Solution -------------------------------------------------------
    prefix_counts: dict[int, int] = {0: 1}  # the empty prefix, seen once
    running = 0
    count = 0
    for value in nums:
        running += value
        count += prefix_counts.get(running - k, 0)
        prefix_counts[running] = prefix_counts.get(running, 0) + 1
    return count


def _brute_force_count(nums: list[int], k: int) -> int:
    """O(n^2) reference: try every start and extend it to the right."""
    count = 0
    for start in range(len(nums)):
        total = 0
        for end in range(start, len(nums)):
            total += nums[end]
            if total == k:
                count += 1
    return count


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's example
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2  # [3] and [1, 2]

    # Empty prefix: a matching subarray that starts at index 0
    assert subarray_sum([1, 2, 3], 6) == 1  # whole array
    assert subarray_sum([3], 3) == 1
    assert subarray_sum([0, 0, 0], 0) == 6  # every subarray of zeros

    # No match, empty input, single element
    assert subarray_sum([], 0) == 0
    assert subarray_sum([], 5) == 0
    assert subarray_sum([1], 0) == 0
    assert subarray_sum([1, 2], 100) == 0

    # Negatives make the running sum non-monotone: both directions must count
    assert subarray_sum([1, -1, 0], 0) == 3  # [1,-1], [0], [1,-1,0]
    assert subarray_sum([-1, -1, 1], 0) == 1  # [-1,-1,1]
    assert subarray_sum([1, -1, 1, -1], 0) == 4
    assert subarray_sum([2, -2, 2, -2], 2) == 3

    # Repeated prefix values each contribute their own subarray
    assert subarray_sum([0, 0, 0, 0], 0) == 10
    assert subarray_sum([1, 1, 1, 1, 1], 3) == 3

    # A large target, a very negative target, and a big value
    assert subarray_sum([10 ** 9, -10 ** 9], 0) == 1
    assert subarray_sum([10 ** 6], -10 ** 6) == 0

    # The caller's list is never mutated
    nums = [1, 2, 3]
    assert subarray_sum(nums, 3) == 2
    assert nums == [1, 2, 3]

    # Exhaustive differential check on tiny arrays against the brute force
    for size in range(0, 6):
        for values in _tuples_of(range(-2, 3), size):
            nums = list(values)
            for k in range(-3, 4):
                assert subarray_sum(nums, k) == _brute_force_count(nums, k), (
                    nums,
                    k,
                )

    # Randomized check on larger arrays, with zeros and negatives included
    rng = random.Random(20261110)
    for _ in range(400):
        size = rng.randint(0, 40)
        nums = [rng.randint(-5, 5) for _ in range(size)]
        k = rng.randint(-10, 10)
        assert subarray_sum(nums, k) == _brute_force_count(nums, k), (nums, k)

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
