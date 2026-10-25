"""
Problem:  <name>                          # e.g. Two Sum
Day:      <NNN>                            # must match ROADMAP.md, e.g. 021
Topic:    <NN-topic-name>                  # e.g. 06-hashing
Difficulty: Easy | Medium | Hard
Platform: LeetCode | HackerRank | Codeforces | GeeksforGeeks | Other
Problem URL: <paste the real URL — leave blank if you do not have one>

Problem Summary:
    <2-4 sentences in your own words. Do not paste the vendor statement.>
Input:
    <types, constraints, what a valid input looks like>
Output:
    <type, what a valid output looks like>

Approach:
    <Step 1, step 2, step 3 — the algorithm, not the code.>
Why This Approach Works:
    <The invariant or mathematical reason this cannot fail.
     If you cannot state it in 1-2 sentences, you do not understand it yet.>

Time Complexity:  O(...)   # justify in one clause: "n iterations + dict lookup"
Space Complexity: O(...)   # justify: "hash map stores at most n entries"

Edge Cases:
    - <empty input>
    - <single element / already solved / no solution>
    - <duplicates, negatives, sorted input, maximum constraints>

Test Cases:
    | input | expected | why |
    |-------|----------|-----|

What I Learned:
    <One pattern, one pitfall, one thing you would do differently.>

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
    assert solve([], 0) == ...              # empty input
    assert solve([1], 1) == ...             # single element
    print("All tests passed.")


if __name__ == "__main__":
    main()
