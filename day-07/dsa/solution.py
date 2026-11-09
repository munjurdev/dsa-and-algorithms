"""
Solution for: Two Sum (Weekly checkpoint 01 — closed-notes re-derivation)
Day:      day-07
Track:    dsa
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Re-derived from a blank file, not opened from `day-04/`. One pass with a
    `value -> index` map of the prefix already scanned. At each index the
    complement `target - value` is looked up in that map; a hit means the
    partner appeared earlier, so the pair is returned immediately. A miss
    stores the current value (overwriting an older duplicate, which keeps the
    map at one entry per distinct value) and moves on. The first index that
    completes a pair is therefore the answer's later index, and the pass never
    re-scans anything.

Time Complexity:  O(n)   # one pass; each dict membership test is O(1) average
Space Complexity: O(n)   # at most one map entry per distinct value

Review Date:  2026-11-10 / 2026-11-16 / 2026-12-09
"""

from __future__ import annotations

import random
from itertools import product


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return the indices of the first pair in `nums` that sums to `target`.

    "First" is by position of the later index: the scan returns as soon as its
    current index completes a pair with something already stored. When several
    earlier positions hold the complement, the most recent one is returned,
    because the map overwrites duplicates as it goes.

    Args:
        nums: array of integers (unsorted, duplicates allowed).
        target: the required sum.

    Returns:
        `[i, j]` with `i < j` and `nums[i] + nums[j] == target`.

    Raises:
        ValueError: if no two distinct indices sum to `target`.
    """
    # --- Solution -------------------------------------------------------
    seen: dict[int, int] = {}  # value -> latest index where it appeared
    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:  # membership, not truthiness: index 0 is falsy
            return [seen[complement], index]
        seen[value] = index
    raise ValueError(f"no pair in {nums!r} sums to {target}")


def _brute_force_pair(nums: list[int], target: int) -> list[int] | None:
    """O(n^2) reference: earliest later index, latest earlier index on a tie.

    The left scan runs backwards so that a duplicate complement reports its
    most recent position, which is exactly what the overwriting map does.
    Returns `None` when no pair exists.
    """
    for right in range(1, len(nums)):
        for left in range(right - 1, -1, -1):
            if nums[left] + nums[right] == target:
                return [left, right]
    return None


def _expect_value_error(nums: list[int], target: int) -> None:
    """Assert that `two_sum` rejects an input with no valid pair."""
    try:
        two_sum(nums, target)
    except ValueError:
        return
    raise AssertionError(f"two_sum({nums!r}, {target}) should raise")


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # LeetCode's canonical cases
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Duplicates: two distinct positions, not one position used twice
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([0, 0], 0) == [0, 1]
    assert two_sum([3, 3, 3], 6) == [0, 1]

    # Negatives, zeros, and a negative target
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]

    # Several valid pairs: the scan must stop at the earliest completing index
    assert two_sum([1, 2, 3, 4, 5], 5) == [1, 2]  # not [0, 3] or [3, 4]
    assert two_sum([2, 1, 3, 1, 2], 4) == [1, 2]
    assert two_sum([2, 2, 1], 4) == [0, 1]

    # No pair at all
    for nums, target in (([], 0), ([1], 1), ([1, 2, 3], 100)):
        _expect_value_error(nums, target)

    # The caller's list is never reordered or extended
    nums = [7, 11, 2, 15]
    assert two_sum(nums, 9) == [0, 2]
    assert nums == [7, 11, 2, 15]

    # Exhaustive differential check on tiny arrays: every input either has no
    # pair, or the returned pair is valid and matches the reference exactly.
    for size in (2, 3, 4):
        for nums_tuple in product(range(-2, 3), repeat=size):
            nums = list(nums_tuple)
            for target in range(-4, 5):
                expected = _brute_force_pair(nums, target)
                if expected is None:
                    _expect_value_error(nums, target)
                else:
                    assert two_sum(nums, target) == expected, (nums, target)

    # Randomized sanity check on larger arrays with a planted pair
    rng = random.Random(20261109)
    for _ in range(300):
        size = rng.randint(2, 60)
        nums = [rng.randint(-10 ** 6, 10 ** 6) for _ in range(size)]
        first, second = rng.sample(range(size), 2)
        target = nums[first] + nums[second]
        left, right = two_sum(nums, target)
        assert 0 <= left < right < size
        assert nums[left] + nums[right] == target

    print("All tests passed.")


if __name__ == "__main__":
    main()
