"""
Solution for: Search in Rotated Sorted Array
Day:      day-12
Track:    dsa
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Keep the ordinary closed-interval binary search, but before comparing the
    target use the midpoint to decide which side is the sorted one: if
    nums[lo] <= nums[mid] the left half is sorted, otherwise the right half is.
    Inside a sorted half a plain range test (lo <= target < mid) says whether
    the target can live there; if it can, search that half, otherwise search
    the other one. The rotated half is never examined by range, only the sorted
    one, which is what keeps every step a halving step.

Time Complexity:  O(log n)  # half-open interval shrinks by half each iteration
Space Complexity: O(1)      # three indices, no auxiliary structures

Review Date:  2026-11-19 (1 day) · 2026-11-25 (7 days) · 2026-12-18 (30 days)
"""

from __future__ import annotations

import random


def search(nums: list[int], target: int) -> int:
    """Return the index of `target` in the rotated sorted array `nums`.

    Args:
        nums: a strictly increasing array rotated at some pivot; may be empty.
        target: the value to look for.

    Returns:
        The index of `target`, or `-1` when it is absent.
    """
    # --- Solution -------------------------------------------------------
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid

        if nums[lo] <= nums[mid]:
            # nums[lo:mid + 1] is sorted ascending.
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            # The rotation is inside the left half, so nums[mid:hi + 1] is sorted.
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return -1


def _brute_force(nums: list[int], target: int) -> int:
    """O(n) reference: first index of `target`, or -1."""
    for index, value in enumerate(nums):
        if value == target:
            return index
    return -1


def _rotations(ordered: list[int]):
    """Yield every rotation of `ordered` — the valid inputs for this problem."""
    for cut in range(len(ordered)):
        yield ordered[cut:] + ordered[:cut]


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's examples
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1

    # Edge cases: empty, single element, two elements without rotation
    assert search([], 5) == -1
    assert search([], -1) == -1
    assert search([1], 1) == 0
    assert search([1, 3], 3) == 1
    assert search([3, 1], 1) == 1
    assert search([1, 2, 3, 4, 5, 6], 4) == 3

    # Targets at the rotation pivot and at both ends
    assert search([5, 1, 3], 5) == 0
    assert search([5, 1, 3], 3) == 2
    assert search([4, 5, 6, 7, 0, 1, 2], 4) == 0
    assert search([4, 5, 6, 7, 0, 1, 2], 2) == 6
    assert search([4, 5, 6, 7, 0, 1, 2], 7) == 3
    assert search([4, 5, 6, 7, 0, 1, 2], 1) == 5

    # Negatives and values outside the array
    assert search([3, -2, -1, 0, 1], -1) == 2
    assert search([3, -2, -1, 0, 1], 5) == -1
    assert search([3, -2, -1, 0, 1], -3) == -1

    # Every rotation of every small sorted array, against the linear oracle
    for size in range(0, 7):
        ordered = list(range(size))
        for candidate in _rotations(ordered):
            for target in range(-2, size + 2):
                got = search(candidate, target)
                want = _brute_force(candidate, target)
                assert got == want, (candidate, target, got, want)

    # Randomized differential check on wider values and larger arrays
    rng = random.Random(20261118)
    for _ in range(500):
        size = rng.randint(0, 60)
        ordered = sorted(rng.sample(range(-200, 200), size))
        cut = rng.randrange(size) if size else 0
        candidate = ordered[cut:] + ordered[:cut]
        target = rng.randint(-220, 220)
        got = search(candidate, target)
        want = _brute_force(candidate, target)
        assert got == want, (candidate, target, got, want)

    print("All tests passed.")


if __name__ == "__main__":
    main()
