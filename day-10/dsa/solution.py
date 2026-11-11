"""
Solution for: Longest Substring Without Repeating Characters
Day:      day-10
Track:    dsa
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Expand a window to the right one character at a time, remembering the last
    index where each character appeared. When the incoming character was seen
    at or after the window's left edge, the window is invalid, so jump `left`
    to one past that occurrence — every shorter window ending here is then
    duplicate-free. Record the character's new index and the window length
    after each step; the answer is the largest length seen.

Time Complexity:  O(n)   # each index enters and leaves the window at most once
Space Complexity: O(min(n, σ))  # last-seen index per distinct character, σ = alphabet size
"""

from __future__ import annotations

import random


def length_of_longest_substring(s: str) -> int:
    """Return the length of the longest substring of `s` with no repeats.

    Args:
        s: any string; may be empty and may contain any Unicode characters.

    Returns:
        The length of the longest contiguous run of characters in which no
        character appears twice. An empty string returns `0`.
    """
    # --- Solution -------------------------------------------------------
    last_seen: dict[str, int] = {}
    left = 0
    best = 0
    for right, char in enumerate(s):
        previous = last_seen.get(char)
        if previous is not None and previous >= left:
            # The character is inside the window: drop everything up to it.
            left = previous + 1
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best


def _brute_force_length(s: str) -> int:
    """O(n^3) reference: test every substring for duplicate characters."""
    best = 0
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if len(set(piece)) == len(piece):
                best = max(best, len(piece))
    return best


def _set_window_length(s: str) -> int:
    """O(n) reference with a plain set: shrink one character at a time.

    Included as a second oracle so the jump-`left` optimization is checked
    against the textbook expand/shrink loop, not only against brute force.
    """
    seen: set[str] = set()
    left = 0
    best = 0
    for right, char in enumerate(s):
        while char in seen:
            seen.remove(s[left])
            left += 1
        seen.add(char)
        best = max(best, right - left + 1)
    return best


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's examples
    assert length_of_longest_substring("abcabcbb") == 3  # "abc"
    assert length_of_longest_substring("bbbbb") == 1  # "b"
    assert length_of_longest_substring("pwwkew") == 3  # "wke", not "pwke"

    # Degenerate inputs
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring(" ") == 1
    assert length_of_longest_substring("a") == 1

    # The classic trap: after "abba", `left` must not move backwards
    assert length_of_longest_substring("abba") == 2
    assert length_of_longest_substring("dvdf") == 3  # "vdf"
    assert length_of_longest_substring("tmmzuxt") == 5  # "mzuxt"

    # Whole string distinct / whole string identical
    assert length_of_longest_substring("abcdef") == 6
    assert length_of_longest_substring("aaaaaa") == 1

    # Characters outside ASCII and multi-byte text
    # ("বাংলা" has two "া" characters, so the best run is "বাংল")
    assert length_of_longest_substring("বাংলা") == 4
    assert length_of_longest_substring("🙂🙂🙃") == 2
    assert length_of_longest_substring("a1b2c3!@#") == 9

    # Digits, spaces, and punctuation are ordinary characters
    assert length_of_longest_substring("ab c d e") == 4  # "ab c"
    assert length_of_longest_substring("???!!") == 2

    # Exhaustive differential check over a tiny alphabet
    # (repeated characters are what the jump-`left` rule has to get right)
    for size in range(0, 8):
        for chars in _strings_of("abc", size):
            assert length_of_longest_substring(chars) == _brute_force_length(chars), chars
            assert length_of_longest_substring(chars) == _set_window_length(chars), chars

    # Randomized check on longer strings over a small alphabet
    rng = random.Random(20261111)
    for _ in range(500):
        size = rng.randint(0, 60)
        chars = "".join(rng.choice("abcd") for _ in range(size))
        assert length_of_longest_substring(chars) == _brute_force_length(chars), chars
        assert length_of_longest_substring(chars) == _set_window_length(chars), chars

    # Randomized check over a wider alphabet: a long distinct run must appear
    for _ in range(200):
        size = rng.randint(0, 40)
        chars = "".join(chr(rng.randint(ord("a"), ord("z"))) for _ in range(size))
        assert length_of_longest_substring(chars) == _set_window_length(chars), chars

    print("All tests passed.")


def _strings_of(alphabet: str, size: int):
    """Yield every string of length `size` over `alphabet` (order matters)."""
    if size == 0:
        yield ""
        return
    for head in alphabet:
        for tail in _strings_of(alphabet, size - 1):
            yield head + tail


if __name__ == "__main__":
    main()
