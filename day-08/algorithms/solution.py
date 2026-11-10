"""
Solution for: Container With Most Water
Day:      day-08
Track:    algorithms
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Start with the widest container, one line at each end. Its height is the
    shorter of the two lines, so the area is width times the smaller height.
    Move the pointer on the shorter line inward: keeping it can never help,
    because any narrower container still pays the same shorter height while
    the width shrinks. Repeat until the pointers meet, keeping the best area.

Time Complexity:  O(n)   # one converging pass; every step retires a line
Space Complexity: O(1)   # only the two pointers and the best area
"""

from __future__ import annotations

import random


def max_area(heights: list[int]) -> int:
    """Return the largest water area two lines can hold.

    Args:
        heights: non-negative line heights, at least two lines for a
            meaningful result; shorter inputs return `0`.

    Returns:
        The maximum over all index pairs `i < j` of
        `(j - i) * min(heights[i], heights[j])`.
    """
    # --- Solution -------------------------------------------------------
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        width = right - left
        area = width * min(heights[left], heights[right])
        if area > best:
            best = area
        # The shorter line caps this container; moving the taller one inward
        # keeps that cap and shrinks the width, so only this move is useful.
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return best


def _brute_force_max_area(heights: list[int]) -> int:
    """O(n^2) reference: check every pair of lines."""
    best = 0
    for left in range(len(heights)):
        for right in range(left + 1, len(heights)):
            best = max(best, (right - left) * min(heights[left], heights[right]))
    return best


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's example
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    # Two lines: exactly one container exists
    assert max_area([1, 1]) == 1
    assert max_area([4, 3]) == 3  # shorter line caps it
    assert max_area([3, 4]) == 3

    # Degenerate and small inputs
    assert max_area([]) == 0
    assert max_area([7]) == 0
    assert max_area([0, 0]) == 0
    assert max_area([0, 5, 0]) == 0  # any pair includes a zero line

    # Flat, increasing, and decreasing profiles
    assert max_area([5, 5, 5, 5]) == 15  # widest pair, equal heights
    assert max_area([1, 2, 3, 4, 5]) == 6  # pair (3, 5): 2 * 3
    assert max_area([5, 4, 3, 2, 1]) == 6

    # Width still matters: two equal tall lines give their widest container
    assert max_area([1000, 1, 1, 1, 1000]) == 4000
    assert max_area([2, 3, 10, 5, 7, 8, 9]) == 36

    # The caller's list is never mutated
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert max_area(heights) == 49
    assert heights == [1, 8, 6, 2, 5, 4, 8, 3, 7]

    # Exhaustive differential check against every-pair search
    for size in range(0, 8):
        for heights_tuple in _tuples_of(range(0, 6), size):
            heights = list(heights_tuple)
            assert max_area(heights) == _brute_force_max_area(heights), heights

    # Randomized differential check on larger profiles
    rng = random.Random(20261110)
    for _ in range(400):
        size = rng.randint(0, 60)
        heights = [rng.randint(0, 10 ** 4) for _ in range(size)]
        assert max_area(heights) == _brute_force_max_area(heights), heights

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
