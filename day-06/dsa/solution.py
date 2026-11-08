"""
Solution for: Merge Intervals
Day:      day-06
Track:    dsa
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Sort the intervals by start (into a new list, so the caller's list is left
    alone), then scan once while building one merged group at a time. An
    interval joins the current group when its start is `<=` the group's end —
    equal ends count, because touching intervals have no gap between them — and
    the group's end becomes the `max` of the two, which keeps a nested interval
    from shrinking it. When an interval starts beyond the group's end, the group
    is closed and a new one begins at that interval.

Time Complexity:  O(n log n)   # sort dominates; the merge scan is one pass
Space Complexity: O(n)         # sorted copy plus at most n output intervals

Review Date:  2026-11-09 / 2026-11-15 / 2026-12-08
"""

from __future__ import annotations

import random


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge every overlapping or touching interval in `intervals`.

    Args:
        intervals: a list of `[start, end]` pairs; any order, `start <= end`,
            intervals may be nested, duplicated, or share an endpoint.

    Returns:
        A new list of disjoint intervals sorted by start, with
        `previous_end < next_start`, whose union equals the input's union.

    Raises:
        ValueError: if an element is not exactly two ints with `start <= end`.
    """
    for interval in intervals:
        if len(interval) != 2:
            raise ValueError(f"interval must be a [start, end] pair: {interval!r}")
        if interval[0] > interval[1]:
            raise ValueError(f"interval start exceeds its end: {interval!r}")

    if not intervals:
        return []

    # --- Solution -------------------------------------------------------
    ordered = sorted(intervals, key=lambda interval: interval[0])
    merged: list[list[int]] = []
    current_start, current_end = ordered[0]

    for start, end in ordered[1:]:
        if start <= current_end:  # overlap *or* touch -> same group
            current_end = max(current_end, end)
        else:
            merged.append([current_start, current_end])
            current_start, current_end = start, end

    merged.append([current_start, current_end])
    return merged


def _reference_merge(intervals: list[list[int]]) -> list[list[int]]:
    """Pairwise fixed-point merge — a different algorithm, used only to test.

    Repeatedly joins any two intervals that overlap or touch, until nothing
    changes, then sorts the survivors. O(n^3) at worst; fine for tiny inputs.
    """
    groups = [list(interval) for interval in intervals]
    changed = True
    while changed:
        changed = False
        for first in range(len(groups)):
            for second in range(first + 1, len(groups)):
                left, right = groups[first], groups[second]
                if left[0] <= right[1] and right[0] <= left[1]:
                    groups[first] = [min(left[0], right[0]), max(left[1], right[1])]
                    groups.pop(second)
                    changed = True
                    break
            if changed:
                break
    groups.sort()
    return groups


def _covered_points(intervals: list[list[int]]) -> set[int]:
    """Every integer point inside any interval — used to compare unions."""
    covered: set[int] = set()
    for start, end in intervals:
        covered.update(range(start, end + 1))
    return covered


def _expect_value_error(intervals: list[list[int]]) -> None:
    """Assert that `merge_intervals` rejects a malformed interval list."""
    try:
        merge_intervals(intervals)
    except ValueError:
        return
    raise AssertionError(f"merge_intervals({intervals!r}) should raise")


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's examples
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([[1, 4], [0, 4]]) == [[0, 4]]
    assert merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]

    # A single interval that swallows every other one
    assert merge_intervals([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]]

    # A real gap must stay a gap
    assert merge_intervals([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]

    # Empty, single, duplicate, zero-length, negatives
    assert merge_intervals([]) == []
    assert merge_intervals([[5, 7]]) == [[5, 7]]
    assert merge_intervals([[1, 2], [1, 2]]) == [[1, 2]]
    assert merge_intervals([[4, 4]]) == [[4, 4]]
    assert merge_intervals([[4, 4], [4, 6]]) == [[4, 6]]
    assert merge_intervals([[-5, -1], [-2, 3], [10, 12]]) == [[-5, 3], [10, 12]]

    # Touching chains collapse to one interval
    assert merge_intervals([[1, 2], [2, 3], [3, 4]]) == [[1, 4]]

    # The caller's list must not be reordered
    unsorted_intervals = [[8, 10], [1, 3], [2, 6], [15, 18]]
    assert merge_intervals(unsorted_intervals) == [[1, 6], [8, 10], [15, 18]]
    assert unsorted_intervals == [[8, 10], [1, 3], [2, 6], [15, 18]]

    # Malformed input is rejected instead of silently ignored
    for malformed in ([[]], [[1]], [[3, 1]], [[1, 2, 3]]):
        _expect_value_error(malformed)

    # Differential check: sort-then-scan must match pairwise fixed-point merge
    rng = random.Random(20261108)
    for _ in range(500):
        count = rng.randint(0, 12)
        case: list[list[int]] = []
        for _ in range(count):
            start = rng.randint(-20, 20)
            case.append([start, start + rng.randint(0, 8)])

        merged = merge_intervals(case)
        assert merged == _reference_merge(case), case

        # Same union: nothing lost, nothing invented
        assert _covered_points(merged) == _covered_points(case), case

        # The output really is disjoint and strictly separated
        for previous, following in zip(merged, merged[1:]):
            assert previous[1] < following[0], case

    # Maximum size: 10^4 intervals that all overlap collapse to one
    big = [[index, 10_000] for index in range(10_000)]
    assert merge_intervals(big) == [[0, 10_000]]

    print("All tests passed.")


if __name__ == "__main__":
    main()
