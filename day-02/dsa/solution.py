"""
Solution for: Valid Anagram
Day:      day-02
Track:    dsa
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Reject on a length mismatch, then build a character-frequency dict from
    `s` in one pass and decrement it while walking `t`, bailing out the
    moment any count goes negative. With equal lengths and no negative
    count, every entry must end at zero, so the strings are an anagram.

Time Complexity:  O(n)   # one pass over each string, O(1) dict operations
Space Complexity: O(1)   # at most 26 entries for lowercase English letters

Review Date:  2026-11-02 / 2026-11-08 / 2026-12-01
"""

from __future__ import annotations


def is_anagram(s: str, t: str) -> bool:
    """Return True when `t` holds exactly the characters of `s`.

    Args:
        s: reference string; case-sensitive, may be empty.
        t: candidate string compared against `s`.

    Returns:
        True if both strings have identical character multiplicities.
    """
    if len(s) != len(t):
        return False
    counts: dict[str, int] = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for char in t:
        counts[char] = counts.get(char, 0) - 1
        if counts[char] < 0:
            return False
    return all(count == 0 for count in counts.values())


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # Typical case
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    # Edge cases
    assert is_anagram("", "") is True       # both empty
    assert is_anagram("a", "ab") is False   # length guard
    assert is_anagram("a", "a") is True     # single element
    assert is_anagram("a", "b") is False    # single mismatch
    print("All tests passed.")


if __name__ == "__main__":
    main()
