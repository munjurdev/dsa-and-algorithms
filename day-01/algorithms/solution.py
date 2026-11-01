"""
Solution for: FizzBuzz + top-k frequency drill
Day:      day-01
Track:    algorithms
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    FizzBuzz: one pass over 1..limit testing divisibility by 15 first, then
    3, then 5, appending the matching label — or `str(number)` — so the list
    holds only strings. Top-k: `Counter` counts every item in a single pass;
    `sorted` on `(-count, word)` ranks frequencies descending with an
    alphabetical tie-break; slicing takes the first k.

Time Complexity:  FizzBuzz O(n) · top-k O(m + u log u)   # n limit, m items, u distinct
Space Complexity: FizzBuzz O(n) · top-k O(u)             # output list + counter

Review Date:  2026-11-02 / 2026-11-08 / 2026-12-01
"""

from __future__ import annotations

from collections import Counter


def fizz_buzz(limit: int) -> list[str]:
    """Return the FizzBuzz sequence for 1..`limit` inclusive.

    Args:
        limit: inclusive upper bound; 0 or less yields an empty list.

    Returns:
        One string per number: "FizzBuzz", "Fizz", "Buzz", or the number.
    """
    if limit < 1:
        return []
    results: list[str] = []
    for number in range(1, limit + 1):
        if number % 15 == 0:
            results.append("FizzBuzz")
        elif number % 3 == 0:
            results.append("Fizz")
        elif number % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(number))
    return results


def top_k_frequent(items: list[str], k: int) -> list[str]:
    """Return the `k` most frequent words in `items`, ties broken alphabetically.

    Args:
        items: words to count; may be empty and may contain duplicates.
        k: how many distinct words to return; clamped by the early return
            when non-positive, and by slicing when larger than the number
            of distinct words.

    Returns:
        Up to `k` words ordered by descending frequency.
    """
    if k <= 0:
        return []
    counts: Counter[str] = Counter(items)
    ranked: list[tuple[str, int]] = sorted(
        counts.items(), key=lambda entry: (-entry[1], entry[0])
    )
    return [word for word, _count in ranked[:k]]


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # FizzBuzz — typical case
    sequence: list[str] = fizz_buzz(15)
    assert len(sequence) == 15
    assert sequence[0] == "1"         # plain number
    assert sequence[2] == "Fizz"      # 3
    assert sequence[4] == "Buzz"      # 5
    assert sequence[14] == "FizzBuzz"  # 15
    # FizzBuzz — edge cases
    assert fizz_buzz(0) == []         # empty input
    assert fizz_buzz(1) == ["1"]      # single element

    # Top-k — typical case
    assert top_k_frequent(["a", "b", "a", "c", "b", "a"], 2) == ["a", "b"]
    # Top-k — edge cases
    assert top_k_frequent([], 3) == []               # empty input
    assert top_k_frequent(["x", "y"], 5) == ["x", "y"]  # k > distinct words
    assert top_k_frequent(["b", "a", "b", "a"], 2) == ["a", "b"]  # tie
    assert top_k_frequent(["a", "a"], 0) == []       # k = 0
    print("All tests passed.")


if __name__ == "__main__":
    main()
