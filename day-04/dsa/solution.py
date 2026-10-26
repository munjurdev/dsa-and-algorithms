"""
Solution for: <name>                       # e.g. Two Sum
Day:      day-04                            # must match the folder, e.g. day-07
Track:    dsa                               # must match the folder this file sits in
Difficulty: Easy | Medium | Hard

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    <the algorithm in words — the detail belongs in problem.md>

Time Complexity:  O(...)   # justify in one clause
Space Complexity: O(...)   # justify in one clause

Review Date:  <YYYY-MM-DD — schedule 1 day, 7 days, and 30 days out>
"""

from __future__ import annotations


def solve(nums: list[int], target: int) -> int:
    """Replace `solve` with a descriptive name once the problem is clear.

    Args:
        nums: <input description>
        target: <what it means>

    Returns:
        <what the caller gets back>

    Raises:
        ValueError: <only if the problem defines invalid input behavior>
    """
    # --- Solution -------------------------------------------------------
    # Keep this section honest: only code you understand line by line.
    raise NotImplementedError


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # Typical case
    assert solve([2, 7, 11, 15], 9) == ...  # expected: fill in
    # Edge cases
    assert solve([], 0) == ...               # empty input
    assert solve([1], 1) == ...              # single element
    print("All tests passed.")


if __name__ == "__main__":
    main()
