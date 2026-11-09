"""
Solution for: Weekly checkpoint 01 — timed re-solve of 4 problems from Days 01–06
Day:      day-07
Track:    algorithms
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Four functions rebuilt from blank files with the notes closed: `is_anagram`
    (frequency map, decrement while scanning, negative count means a surplus
    character), `max_subarray` (Kadane, seeded from the first element so the
    all-negative case answers the largest single value), `spiral_order` (four
    shrinking boundaries, with the bottom and left edges guarded), and
    `merge_intervals` (sort by start, then merge while `start <= current_end`
    and keep the `max` of the ends). Each is checked against a different
    reference algorithm so a memorised expected list cannot hide a mistake.

Time Complexity:  O(n) / O(n) / O(m·n) / O(n log n) — see per function below
Space Complexity: O(k) / O(1) / O(1) / O(n)          — see per function below

Review Date:  2026-11-10 / 2026-11-16 / 2026-12-09
"""

from __future__ import annotations

import random

# The four problems this checkpoint re-solves, in the order they were attempted.
RESOLVED = (
    "valid anagram (day-02)",
    "maximum subarray (day-04)",
    "spiral matrix (day-05)",
    "merge intervals (day-06)",
)


def is_anagram(s: str, t: str) -> bool:
    """Return whether `s` and `t` are anagrams (same characters, same counts).

    Time O(n), space O(k) for k distinct characters.
    """
    if len(s) != len(t):
        return False

    # --- Solution -------------------------------------------------------
    remaining: dict[str, int] = {}
    for character in s:
        remaining[character] = remaining.get(character, 0) + 1
    for character in t:
        if remaining.get(character, 0) == 0:
            return False  # `t` has one character too many
        remaining[character] -= 1
    return True


def max_subarray(nums: list[int]) -> int:
    """Return the largest sum of a non-empty contiguous subarray.

    Time O(n), space O(1). Raises `ValueError` on empty input.

    --- Solution -------------------------------------------------------
    Kadane: `best_ending_here` is the best run that ends at the current index,
    either extending the previous run or restarting at the current value.
    Seeding both registers from `nums[0]` keeps the empty subarray out of the
    answer, so an all-negative input returns its largest single element.
    """
    if not nums:
        raise ValueError("nums must contain at least one element")

    best_ending_here = nums[0]
    best = nums[0]
    for value in nums[1:]:
        best_ending_here = max(value, best_ending_here + value)
        best = max(best, best_ending_here)
    return best


def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Return the values of a rectangular matrix in clockwise spiral order.

    Time O(m·n), space O(1) auxiliary. Raises `ValueError` for a grid with no
    columns or with rows of different lengths.
    """
    if not matrix:
        return []

    columns = len(matrix[0])
    for row in matrix:
        if len(row) != columns:
            raise ValueError(f"matrix rows must be rectangular: {matrix!r}")
    if columns == 0:
        raise ValueError("matrix must have at least one column")

    # --- Solution -------------------------------------------------------
    top, bottom = 0, len(matrix) - 1
    left, right = 0, columns - 1
    order: list[int] = []

    while top <= bottom and left <= right:
        for column in range(left, right + 1):
            order.append(matrix[top][column])
        top += 1

        for row in range(top, bottom + 1):
            order.append(matrix[row][right])
        right -= 1

        if top <= bottom:  # a row still remains after the top edge
            for column in range(right, left - 1, -1):
                order.append(matrix[bottom][column])
            bottom -= 1

        if left <= right:  # a column still remains after the right edge
            for row in range(bottom, top - 1, -1):
                order.append(matrix[row][left])
            left += 1

    return order


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """Merge overlapping or touching `[start, end]` intervals.

    Time O(n log n), space O(n) for the sorted copy and the output. Raises
    `ValueError` for anything that is not a `[start, end]` pair with
    `start <= end`.
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
        if start <= current_end:  # overlap or touch -> same group
            current_end = max(current_end, end)  # `max` keeps nesting intact
        else:
            merged.append([current_start, current_end])
            current_start, current_end = start, end

    merged.append([current_start, current_end])
    return merged


# ---------------------------------------------------------------------------
# References — different algorithms, used only to differential-test the above
# ---------------------------------------------------------------------------


def _brute_force_max_subarray(nums: list[int]) -> int:
    """O(n^2) maximum subarray over every slice."""
    best = nums[0]
    for left in range(len(nums)):
        running = 0
        for right in range(left, len(nums)):
            running += nums[right]
            best = max(best, running)
    return best


def _direction_walk_spiral(matrix: list[list[int]]) -> list[int]:
    """Spiral by walking right/down/left/up and turning at the visited edge."""
    rows, columns = len(matrix), len(matrix[0])
    visited: set[tuple[int, int]] = set()
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    row = column = 0
    heading = 0
    order: list[int] = []

    for _ in range(rows * columns):
        order.append(matrix[row][column])
        visited.add((row, column))
        next_row, next_column = (
            row + directions[heading][0],
            column + directions[heading][1],
        )
        if (
            0 <= next_row < rows
            and 0 <= next_column < columns
            and (next_row, next_column) not in visited
        ):
            row, column = next_row, next_column
        else:
            heading = (heading + 1) % 4
            row += directions[heading][0]
            column += directions[heading][1]
    return order


def _reference_merge(intervals: list[list[int]]) -> list[list[int]]:
    """Pairwise fixed-point merge — a different algorithm, used only to test."""
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
    """Every integer point inside any interval, used to compare unions."""
    covered: set[int] = set()
    for start, end in intervals:
        covered.update(range(start, end + 1))
    return covered


def _expect_value_error(function, argument) -> None:
    """Assert that `function(argument)` rejects malformed input."""
    try:
        function(argument)
    except ValueError:
        return
    raise AssertionError(f"{function.__name__}({argument!r}) should raise")


def main() -> None:
    """Run the checkpoint suite. All four re-solves must pass before done."""
    assert len(RESOLVED) == 4  # checkpoint target: four closed-notes re-solves

    # 1. Valid Anagram — LeetCode cases, duplicates, case sensitivity
    assert is_anagram("anagram", "nagaram")
    assert not is_anagram("rat", "car")
    assert is_anagram("", "")
    assert not is_anagram("a", "ab")
    assert is_anagram("aabb", "abab")
    assert not is_anagram("aabb", "abbb")  # equal sets, different counts
    assert not is_anagram("Anagram", "nagaram")  # case-sensitive

    # 2. Maximum Subarray — statement cases and the all-negative trap
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([1]) == 1
    assert max_subarray([-3, -1, -2]) == -1  # never the empty sum
    assert max_subarray([0, -1]) == 0
    _expect_value_error(max_subarray, [])

    # 3. Spiral Matrix — every degenerate shape, including one row/column
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5,
    ]
    assert spiral_order([[1, 2, 3]]) == [1, 2, 3]
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]
    assert spiral_order([[7]]) == [7]
    assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]
    assert spiral_order([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 6, 5, 4]
    assert spiral_order([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]
    assert spiral_order([]) == []
    _expect_value_error(spiral_order, [[]])
    _expect_value_error(spiral_order, [[1, 2], [3]])

    # 4. Merge Intervals — touching, nested, duplicates, negatives
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]
    assert merge_intervals([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]
    assert merge_intervals([[1, 2], [1, 2]]) == [[1, 2]]
    assert merge_intervals([[-5, -1], [-2, 3], [10, 12]]) == [[-5, 3], [10, 12]]
    assert merge_intervals([]) == []
    for malformed in ([[]], [[1]], [[3, 1]], [[1, 2, 3]]):
        _expect_value_error(merge_intervals, malformed)

    # Differential checks — each against a different reference algorithm
    rng = random.Random(20261109)

    # Anagram oracle: sorted() comparison is exact and independent of counting
    for _ in range(300):
        first = "".join(rng.choice("abc") for _ in range(rng.randint(0, 8)))
        if rng.random() < 0.5:
            second = "".join(rng.choice("abc") for _ in range(rng.randint(0, 8)))
        else:
            letters = list(first)
            rng.shuffle(letters)
            second = "".join(letters)
        assert is_anagram(first, second) == (sorted(first) == sorted(second))

    # Kadane vs brute force over every slice
    for _ in range(300):
        size = rng.randint(1, 25)
        nums = [rng.randint(-10, 10) for _ in range(size)]
        assert max_subarray(nums) == _brute_force_max_subarray(nums), nums

    # Spiral vs direction walk over every small shape
    for rows in range(1, 7):
        for columns in range(1, 7):
            matrix = [
                [rng.randint(0, 99) for _ in range(columns)] for _ in range(rows)
            ]
            assert spiral_order(matrix) == _direction_walk_spiral(matrix), matrix
            assert sorted(spiral_order(matrix)) == sorted(
                value for row in matrix for value in row
            )

    # Merge intervals vs pairwise fixed point, plus a union-coverage check
    for _ in range(300):
        count = rng.randint(0, 10)
        case: list[list[int]] = []
        for _ in range(count):
            start = rng.randint(-15, 15)
            case.append([start, start + rng.randint(0, 8)])
        merged = merge_intervals(case)
        assert merged == _reference_merge(case), case
        assert _covered_points(merged) == _covered_points(case), case
        for previous, following in zip(merged, merged[1:]):
            assert previous[1] < following[0], case

    print("All tests passed.")


if __name__ == "__main__":
    main()
