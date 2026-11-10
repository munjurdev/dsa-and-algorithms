"""
Solution for: 3Sum
Day:      day-08
Track:    dsa
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Sort the array, then fix one value at a time and solve the remaining
    two-sum with converging pointers. Because the array is sorted, a total
    below zero can only be repaired by moving `left` right, and a total above
    zero only by moving `right` left. Equal fixed values and equal values
    immediately after a match are skipped, so every triplet is emitted once.

Time Complexity:  O(n^2)   # n fixed positions, each with one linear two-pointer scan
Space Complexity: O(1)     # beyond the sorted copy and the output list
"""

from __future__ import annotations

import random
from itertools import combinations


def three_sum(nums: list[int]) -> list[list[int]]:
    """Return every unique triplet of distinct indices that sums to zero.

    The result is sorted, and each triplet is in ascending order. Duplicate
    values in the input do not produce duplicate triplets.

    Args:
        nums: array of integers, unsorted, duplicates allowed.

    Returns:
        `[[a, b, c], ...]` with `a <= b <= c`, `a + b + c == 0`, no repeats.
    """
    # --- Solution -------------------------------------------------------
    ordered = sorted(nums)
    triplets: list[list[int]] = []
    n = len(ordered)

    for fixed in range(n - 2):
        value = ordered[fixed]

        # Sorted: once the smallest available value is positive, so is the sum.
        if value > 0:
            break
        # Skip a duplicate fixed value: it would rebuild the same triplets.
        if fixed > 0 and value == ordered[fixed - 1]:
            continue

        left, right = fixed + 1, n - 1
        while left < right:
            total = value + ordered[left] + ordered[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([value, ordered[left], ordered[right]])
                left += 1
                right -= 1
                # Skip duplicates on both sides of the match.
                while left < right and ordered[left] == ordered[left - 1]:
                    left += 1
                while left < right and ordered[right] == ordered[right + 1]:
                    right -= 1

    return triplets


def _brute_force_three_sum(nums: list[int]) -> list[list[int]]:
    """O(n^3) reference: every index triple, deduplicated as sorted tuples."""
    found = {
        tuple(sorted(combo))
        for combo in combinations(nums, 3)
        if combo[0] + combo[1] + combo[2] == 0
    }
    return [list(triplet) for triplet in sorted(found)]


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's example: two distinct triplets
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

    # No triplet possible
    assert three_sum([]) == []
    assert three_sum([0]) == []
    assert three_sum([1, 2]) == []
    assert three_sum([1, 2, 3]) == []  # all positive, early break
    assert three_sum([-3, -2, -1]) == []  # all negative

    # All zeros: one triplet, not C(n, 3) of them
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]

    # Duplicates around a valid triplet must not repeat it
    assert three_sum([-1, 0, 1, 0]) == [[-1, 0, 1]]
    assert three_sum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
    assert three_sum([-1, -1, -1, 2, 2, 2]) == [[-1, -1, 2]]

    # Zero triplets of mixed shapes, and repeated fixed values
    assert three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]) == [
        [-4, -2, 6],
        [-4, 0, 4],
        [-4, 1, 3],
        [-4, 2, 2],
        [-2, -2, 4],
        [-2, 0, 2],
    ]

    # Negatives and off-by-one neighbours
    assert three_sum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]
    assert three_sum([-5, 2, 3, 0]) == [[-5, 2, 3]]

    # The caller's list is never reordered
    nums = [3, -1, -1, 2, -4]
    assert three_sum(nums) == [[-1, -1, 2]]
    assert nums == [3, -1, -1, 2, -4]

    # Exhaustive differential check on tiny arrays against the brute force
    for size in range(0, 7):
        for values in _tuples_of(range(-3, 4), size):
            nums = list(values)
            assert three_sum(nums) == _brute_force_three_sum(nums), nums

    # Randomized check on larger arrays with duplicates planted deliberately
    rng = random.Random(20261110)
    for _ in range(300):
        size = rng.randint(0, 30)
        nums = [rng.randint(-8, 8) for _ in range(size)]
        assert three_sum(nums) == _brute_force_three_sum(nums), nums

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
