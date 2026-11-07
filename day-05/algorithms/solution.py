"""
Solution for: Spiral Matrix
Day:      day-05
Track:    algorithms
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Keep four boundaries around the unvisited rectangle and peel its border
    clockwise each round: the top row left to right, the right column down,
    the bottom row right to left, the left column up — shrinking the matching
    boundary after each edge. The bottom and left edges are guarded by
    `top <= bottom` and `left <= right`, because on a single-row or
    single-column board those edges would otherwise re-emit the row or column
    just consumed. No visited grid is needed, so the extra space is O(1).

Time Complexity:  O(m · n)   # every cell appended exactly once
Space Complexity: O(1)       # four indices; the output list is not counted

Review Date:  2026-11-08 / 2026-11-14 / 2026-12-07
"""

from __future__ import annotations

import random


def spiral_order(matrix: list[list[int]]) -> list[int]:
    """Return the values of `matrix` in clockwise spiral order.

    Args:
        matrix: a rectangular `m x n` grid of integers; rows must be non-empty
            and all the same length.

    Returns:
        A flat list of the `m * n` values, taking the outer ring clockwise and
        then repeating on each inner ring.

    Raises:
        ValueError: if the rows are not all the same non-zero length.
    """
    if not matrix:
        return []
    width = len(matrix[0])
    if width == 0 or any(len(row) != width for row in matrix):
        raise ValueError("matrix must be rectangular with at least one column")

    # --- Solution -------------------------------------------------------
    result: list[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, width - 1

    while top <= bottom and left <= right:
        # Top edge: left -> right
        for column in range(left, right + 1):
            result.append(matrix[top][column])
        top += 1

        # Right edge: top -> bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Bottom edge: right -> left. Skip it when the top edge just took the
        # only remaining row, or it would be emitted twice.
        if top <= bottom:
            for column in range(right, left - 1, -1):
                result.append(matrix[bottom][column])
            bottom -= 1

        # Left edge: bottom -> top. Skip it when the right edge just took the
        # only remaining column.
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


def _reference_spiral(matrix: list[list[int]]) -> list[int]:
    """Direction-walk reference with a visited grid, used only to test above."""
    if not matrix or not matrix[0]:
        return []
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    steps = ((0, 1), (1, 0), (0, -1), (-1, 0))  # right, down, left, up
    row = column = heading = 0
    order: list[int] = []

    for _ in range(rows * cols):
        order.append(matrix[row][column])
        visited[row][column] = True
        next_row, next_column = row + steps[heading][0], column + steps[heading][1]
        if (
            0 <= next_row < rows
            and 0 <= next_column < cols
            and not visited[next_row][next_column]
        ):
            row, column = next_row, next_column
        else:
            heading = (heading + 1) % 4  # turn right against the wall
            row += steps[heading][0]
            column += steps[heading][1]

    return order


def _expect_value_error(matrix: list[list[int]]) -> None:
    """Assert that `spiral_order` rejects a malformed grid."""
    try:
        spiral_order(matrix)
    except ValueError:
        return
    raise AssertionError(f"spiral_order({matrix!r}) should raise")


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's examples
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1, 2, 3, 6, 9, 8, 7, 4, 5,
    ]
    assert spiral_order(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    # 1 x n and n x 1: the shared row/column must not be emitted twice
    assert spiral_order([[1, 2, 3]]) == [1, 2, 3]
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]
    assert spiral_order([[1, 2]]) == [1, 2]
    assert spiral_order([[1], [2]]) == [1, 2]

    # Square boards that end exactly on a ring boundary
    assert spiral_order([[7]]) == [7]
    assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])[-1] == 5
    assert len(spiral_order([[1, 2, 3, 4]] * 4)) == 16

    # Rectangles with a leftover inner row or column
    assert spiral_order([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 6, 5, 4]
    assert spiral_order([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == [
        1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8,
    ]

    # Empty input is fine; a grid with no columns or ragged rows is not
    assert spiral_order([]) == []
    for malformed in ([[]], [[1, 2], [3]], [[1], [2, 3], [4]]):
        _expect_value_error(malformed)

    # Differential check: the four-boundary peel must match a direction walk
    rng = random.Random(20261107)
    for _ in range(400):
        rows, cols = rng.randint(1, 6), rng.randint(1, 6)
        matrix = [[rng.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]
        order = spiral_order(matrix)
        assert order == _reference_spiral(matrix), matrix
        assert len(order) == rows * cols            # nothing duplicated
        assert sorted(order) == sorted(v for row in matrix for v in row)

    # Maximum size: every cell appears exactly once
    big = [[row * 10 + column for column in range(10)] for row in range(10)]
    assert sorted(spiral_order(big)) == list(range(100))
    assert spiral_order(big)[:10] == list(range(10))        # top edge intact
    assert spiral_order(big)[10:19] == [19, 29, 39, 49, 59, 69, 79, 89, 99]

    print("All tests passed.")


if __name__ == "__main__":
    main()
