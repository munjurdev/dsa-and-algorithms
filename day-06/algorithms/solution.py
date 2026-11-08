"""
Solution for: Merge Sort vs `sorted()` (self-made)
Day:      day-06
Track:    algorithms
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Top-down merge sort: split the sequence at its midpoint, sort both halves
    recursively, then merge the two sorted runs with two indices, always taking
    the smaller head and preferring the left run on a tie so the sort stays
    stable. One recursive case is enough — a sequence of length 0 or 1 is
    already sorted. An optional `comparisons` counter (a one-element list,
    passed down through every call) records how many element comparisons the
    merge performed, which lets the tests check the `n * ceil(log2 n)` bound
    instead of merely quoting it. Correctness is established differentially
    against `sorted()`, which is Timsort and never used inside the sort.

Time Complexity:  O(n log n)   # ceil(log2 n) levels, each merging O(n) elements
Space Complexity: O(n)         # peak merged lists plus O(log n) recursion depth

Review Date:  2026-11-09 / 2026-11-15 / 2026-12-08
"""

from __future__ import annotations

import math
import random
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def merge_sort(
    values: Sequence[T],
    comparisons: list[int] | None = None,
) -> list[T]:
    """Return a new list with `values` in non-decreasing order.

    Args:
        values: any sequence of mutually comparable elements (`<=` is enough).
        comparisons: optional one-element list; incremented by the number of
            element comparisons performed, so callers can check the bound.

    Returns:
        A sorted copy of `values`; the input sequence is not modified.
    """
    if len(values) <= 1:  # base case: empty or single element is sorted
        return list(values)

    # --- Solution -------------------------------------------------------
    middle = len(values) // 2
    left = merge_sort(values[:middle], comparisons)
    right = merge_sort(values[middle:], comparisons)
    return _merge(left, right, comparisons)


def _merge(
    left: list[T],
    right: list[T],
    comparisons: list[int] | None = None,
) -> list[T]:
    """Merge two sorted lists into one sorted list.

    Equal elements are taken from `left` first, which is what makes the sort
    stable. Whatever remains of the longer run is already sorted, so it is
    appended unchanged instead of being compared.
    """
    merged: list[T] = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if comparisons is not None:
            comparisons[0] += 1
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Drain the run that still has elements (at most one of these is non-empty)
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # Smallest real merges
    assert merge_sort([3, 1, 2]) == [1, 2, 3]
    assert merge_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]

    # Base cases
    assert merge_sort([]) == []
    assert merge_sort([3]) == [3]

    # Duplicates, all-equal, sorted, reversed, negatives
    assert merge_sort([7, 7, 7, 7]) == [7, 7, 7, 7]
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([-3, 0, -1, 2]) == [-3, -1, 0, 2]

    # Stability: equal keys keep their original relative order
    assert merge_sort([(1, "a"), (1, "b"), (0, "c")]) == [
        (0, "c"),
        (1, "a"),
        (1, "b"),
    ]

    # No mutation, and the result is a new list (even for the base case)
    original = [4, 1, 3, 2]
    sorted_copy = merge_sort(original)
    assert original == [4, 1, 3, 2]
    assert sorted_copy == [1, 2, 3, 4]
    assert sorted_copy is not original
    single = [9]
    assert merge_sort(single) is not single

    # Differential check against Timsort on random input
    rng = random.Random(20261108)
    for _ in range(500):
        values = [rng.randint(-50, 50) for _ in range(rng.randint(0, 60))]
        assert merge_sort(values) == sorted(values), values

    # The comparison count must stay inside the derived n * ceil(log2 n) bound
    for size in (1, 2, 3, 5, 8, 16, 64, 256):
        values = [rng.randint(-1000, 1000) for _ in range(size)]
        counter = [0]
        assert merge_sort(values, counter) == sorted(values)
        if size <= 1:
            assert counter[0] == 0, (size, counter[0])
        else:
            bound = size * math.ceil(math.log2(size))
            assert counter[0] <= bound, (size, counter[0], bound)

    # Already-sorted and reverse-sorted inputs also respect the bound
    for values in (list(range(300)), list(range(300, 0, -1))):
        counter = [0]
        assert merge_sort(values, counter) == sorted(values)
        assert counter[0] <= len(values) * math.ceil(math.log2(len(values)))

    # Constraint-size sanity check: 10^4 values, depth is about 14
    large = [rng.randint(-10_000, 10_000) for _ in range(10_000)]
    assert merge_sort(large) == sorted(large)

    print("All tests passed.")


if __name__ == "__main__":
    main()
