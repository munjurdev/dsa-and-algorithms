"""
Solution for: Reverse Words in a String
Day:      day-01
Track:    dsa
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Split the input on whitespace with `str.split()` (no argument), which
    drops leading, trailing, and repeated spaces and yields the words in
    their original order. Reverse the resulting list with `[::-1]` and join
    with a single space — exactly the normalised output the problem wants.

Time Complexity:  O(n)   # one split pass + one join pass over n characters
Space Complexity: O(n)   # the word list stores at most n characters

Review Date:  2026-11-02 / 2026-11-08 / 2026-12-01
"""

from __future__ import annotations


def reverse_words(sentence: str) -> str:
    """Return `sentence` with its words reversed and whitespace normalised.

    Args:
        sentence: raw text; words are separated by arbitrary whitespace runs.

    Returns:
        Words in reverse order joined by single spaces; `""` for blank input.
    """
    words: list[str] = sentence.split()
    return " ".join(words[::-1])


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # Typical case
    assert reverse_words("the sky is blue") == "blue is sky the"
    # Edge cases
    assert reverse_words("") == ""                              # empty input
    assert reverse_words("   ") == ""                           # whitespace only
    assert reverse_words("a") == "a"                            # single element
    assert reverse_words("  hello   world  ") == "world hello"  # space runs
    print("All tests passed.")


if __name__ == "__main__":
    main()
