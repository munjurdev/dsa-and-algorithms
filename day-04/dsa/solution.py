"""
Solution for: Two Sum
Day:      day-04
Track:    dsa
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    One pass with a `value -> index` map of the prefix already scanned. At
    each index the complement `target - value` is looked up in that map; a hit
    means the partner has already been seen, so both indices are returned
    immediately. A miss stores the current value and continues. Nothing is
    ever scanned twice, so the pass is linear and the map never exceeds the
    input size.

Time Complexity:  O(n)   # one pass, each dict lookup is O(1) on average
Space Complexity: O(n)   # the map holds at most one entry per element

Review Date:  2026-11-06 / 2026-11-12 / 2026-12-05
"""

from __future__ import annotations

import random


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return the indices of the two values in `nums` that add up to `target`.

    Args:
        nums: array of integers (unsorted, duplicates allowed).
        target: the required sum.

    Returns:
        `[i, j]` with `i < j` and `nums[i] + nums[j] == target`.

    Raises:
        ValueError: if no two distinct indices sum to `target`.
    """
    # --- Solution -------------------------------------------------------
    seen: dict[int, int] = {}  # value -> most recent index where it appeared
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:  # `in`, not truthiness: index 0 is falsy
            return [seen[complement], index]
        seen[value] = index
    raise ValueError(f"no pair in {nums!r} sums to {target}")


def _has_pair(nums: list[int], target: int) -> bool:
    """O(n^2) reference predicate, used only to differential-test above."""
    return any(
        nums[left] + nums[right] == target
        for left in range(len(nums))
        for right in range(left + 1, len(nums))
    )


def _expect_value_error(nums: list[int], target: int) -> None:
    """Assert that `two_sum` rejects an input with no valid pair."""
    try:
        two_sum(nums, target)
    except ValueError:
        return
    raise AssertionError(f"two_sum({nums!r}, {target}) should raise")


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # Typical case, plus an answer that is not simply the first two elements
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Edge cases: duplicates, negatives, zeros
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]
    assert two_sum([0, 0], 0) == [0, 1]
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

    # No valid pair
    for nums, target in (([], 0), ([1], 1), ([1, 2, 3], 100)):
        _expect_value_error(nums, target)

    # Exhaustive differential check on tiny arrays: `two_sum` must return a
    # valid pair exactly when one exists, and reject the input otherwise.
    from itertools import product

    for size in (2, 3, 4):
        for nums_tuple in product(range(-2, 3), repeat=size):
            nums = list(nums_tuple)
            for target in range(-4, 5):
                if _has_pair(nums, target):
                    left, right = two_sum(nums, target)
                    assert left < right
                    assert nums[left] + nums[right] == target
                else:
                    _expect_value_error(nums, target)

    # Randomized sanity check on larger arrays with a planted pair
    rng = random.Random(20261105)
    for _ in range(200):
        size = rng.randint(2, 50)
        nums = [rng.randint(-10 ** 6, 10 ** 6) for _ in range(size)]
        first, second = rng.sample(range(size), 2)
        target = nums[first] + nums[second]
        left, right = two_sum(nums, target)
        assert left < right
        assert nums[left] + nums[right] == target

    print("All tests passed.")


if __name__ == "__main__":
    main()
