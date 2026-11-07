"""
Solution for: Valid Palindrome
Day:      day-05
Track:    dsa
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Normalise implicitly: only ASCII letters and digits are kept, and letters
    are lowercased. `is_palindrome` walks two pointers inward, each skip loop
    jumping over non-alphanumeric characters, and compares the characters they
    land on — no copy is ever built. `is_palindrome_normalized` does the same
    comparison the obvious way: build the cleaned string, compare it with its
    reverse. Both share one predicate, so they can disagree only if the
    two-pointer scan is wrong, which is what the tests check.

Time Complexity:  O(n)   # each character examined once per pointer / once by the filter
Space Complexity: O(1)   # two indices; the normalised variant is O(n) for the copy

Review Date:  2026-11-08 / 2026-11-14 / 2026-12-07
"""

from __future__ import annotations

import random
import string
from itertools import product


def _is_ascii_alphanumeric(char: str) -> bool:
    """Return True for `0-9`, `a-z`, `A-Z` only — LeetCode's definition.

    `str.isalnum()` on its own is Unicode-aware and accepts characters such as
    'É' or '²', which the problem does not count as alphanumeric. The
    `isascii()` guard keeps the predicate honest.
    """
    return char.isascii() and char.isalnum()


def is_palindrome(s: str) -> bool:
    """Decide whether `s` is a palindrome ignoring case and non-alphanumerics.

    Args:
        s: the phrase to test; any characters, including Unicode.

    Returns:
        True if the letters and digits of `s`, lowercased, read the same
        forwards and backwards.

    Two pointers moving inward, skipping junk in place — O(1) extra space.
    """
    # --- Solution -------------------------------------------------------
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not _is_ascii_alphanumeric(s[left]):
            left += 1
        while left < right and not _is_ascii_alphanumeric(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_normalized(s: str) -> bool:
    """Same answer via the cleaned string, kept for cross-checking.

    Builds the normalised copy first, so it costs O(n) space instead of O(1);
    it exists to prove the in-place version does the same comparisons.
    """
    cleaned = "".join(
        char.lower() for char in s if _is_ascii_alphanumeric(char)
    )
    return cleaned == cleaned[::-1]


def _reference_is_palindrome(s: str) -> bool:
    """Plain-language check, written differently from both variants."""
    kept = [char.lower() for char in s if _is_ascii_alphanumeric(char)]
    for offset in range(len(kept) // 2):
        if kept[offset] != kept[-1 - offset]:
            return False
    return True


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's two examples
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False

    # No alphanumerics at all: the cleaned string is empty, which is a palindrome
    assert is_palindrome(" ") is True
    assert is_palindrome(".,") is True
    assert is_palindrome("") is True

    # Single character, both kinds
    assert is_palindrome("a") is True
    assert is_palindrome("!") is True

    # Case folding, digits, embedded punctuation
    assert is_palindrome("Aa") is True
    assert is_palindrome("0P") is False     # digits survive cleaning
    assert is_palindrome("ab_a") is True    # underscore is dropped -> "aba"
    assert is_palindrome("1a2") is False
    assert is_palindrome("12321") is True

    # Non-ASCII letters are dropped rather than folded
    assert is_palindrome("Éa") is True

    # Both parities
    assert is_palindrome("abba") is True
    assert is_palindrome("aba") is True

    # The two variants, plus a third reference, must agree everywhere
    alphabet = "aA0_. " + "!zZ9"
    for size in range(5):
        for chars in product(alphabet, repeat=size):
            text = "".join(chars)
            expected = _reference_is_palindrome(text)
            assert is_palindrome(text) is expected, text
            assert is_palindrome_normalized(text) is expected, text

    # Randomized agreement on longer, messier strings
    rng = random.Random(20261107)
    pool = string.ascii_letters + string.digits + " .,!_-:;'\"()" + "éÉ²"
    for _ in range(300):
        text = "".join(rng.choice(pool) for _ in range(rng.randint(0, 40)))
        expected = _reference_is_palindrome(text)
        assert is_palindrome(text) is expected, text
        assert is_palindrome_normalized(text) is expected, text

    # Constraint sanity: the maximum length must be a single linear pass
    long_text = "a!" * 100_000
    assert is_palindrome(long_text) is True
    assert is_palindrome("ab" * 100_000) is False

    print("All tests passed.")


if __name__ == "__main__":
    main()
