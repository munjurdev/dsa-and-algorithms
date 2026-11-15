"""
Solution for: Find All Anagrams in a String
Day:      day-11
Track:    algorithms
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Every anagram of `p` has exactly `len(p)` characters, so the search is a
    fixed-size window whose counts must equal `p`'s counts. Slide a window of
    that width one step at a time, adding the entering character and removing
    the leaving one, and record the start index whenever the window's counts
    match the target counts. Comparing two frequency maps costs at most the
    alphabet size, so the whole scan stays linear.

Time Complexity:  O(n)   # one pass, O(1) map work per step (alphabet is fixed)
Space Complexity: O(σ)   # two count maps over the alphabet, σ ≤ 26
"""

from __future__ import annotations

import random
from collections import Counter


def find_anagrams(s: str, p: str) -> list[int]:
    """Return the start indices of every anagram of `p` inside `s`.

    Args:
        s: the string to search in; may be empty.
        p: the pattern whose anagrams are sought; must be non-empty.

    Returns:
        Ascending list of indices `i` such that `s[i:i + len(p)]` is a
        permutation of `p`. Empty when there is no such window.

    Raises:
        ValueError: if `p` is empty, because an empty pattern would match at
            every index and that is not a meaningful anagram search.
    """
    # --- Solution -------------------------------------------------------
    if not p:
        raise ValueError("pattern p must be non-empty")
    width = len(p)
    if width > len(s):
        return []

    need = Counter(p)
    window: Counter[str] = Counter()
    starts: list[int] = []

    for right, char in enumerate(s):
        window[char] += 1
        if right >= width:
            leaving = s[right - width]
            window[leaving] -= 1
            if window[leaving] == 0:
                del window[leaving]
        if right >= width - 1 and window == need:
            starts.append(right - width + 1)

    return starts


def _brute_force_anagrams(s: str, p: str) -> list[int]:
    """O(n·k log k) reference: sort each length-k window and compare."""
    width = len(p)
    target = sorted(p)
    return [
        start
        for start in range(len(s) - width + 1)
        if sorted(s[start : start + width]) == target
    ]


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's examples
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]
    assert find_anagrams("abab", "ab") == [0, 1, 2]

    # Every index is an anagram, and no index is
    assert find_anagrams("aaaa", "aa") == [0, 1, 2]
    assert find_anagrams("abcdef", "gh") == []

    # Pattern longer than the string, empty string, single character
    assert find_anagrams("ab", "abc") == []
    assert find_anagrams("", "a") == []
    assert find_anagrams("abc", "a") == [0]

    # Whole-string match sits at index 0 only
    assert find_anagrams("abc", "bca") == [0]
    assert find_anagrams("abcabc", "abc") == [0, 1, 2, 3]

    # Repeated characters in the pattern must be counted, not just present
    assert find_anagrams("aabb", "aab") == [0]
    assert find_anagrams("aa", "aaa") == []
    assert find_anagrams("baaab", "aab") == [0, 2]

    # Overlapping matches at consecutive starts
    assert find_anagrams("abababab", "abab") == [0, 1, 2, 3, 4]

    # Non-ASCII input is just characters to be counted
    assert find_anagrams("বাংলা", "বা") == [0]

    # An empty pattern is rejected rather than matching everywhere
    try:
        find_anagrams("abc", "")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for an empty pattern")

    # The caller's strings are never mutated
    source, pattern = "cbaebabacd", "abc"
    assert find_anagrams(source, pattern) == [0, 6]
    assert (source, pattern) == ("cbaebabacd", "abc")

    # Exhaustive differential check over a tiny alphabet
    for s_size in range(0, 6):
        for source in _strings_of("ab", s_size):
            for p_size in range(1, 4):
                for pattern in _strings_of("ab", p_size):
                    got = find_anagrams(source, pattern)
                    want = _brute_force_anagrams(source, pattern)
                    assert got == want, (source, pattern, got, want)

    # Randomized check over a wider alphabet
    rng = random.Random(20261115)
    for _ in range(500):
        source = "".join(rng.choice("abcd") for _ in range(rng.randint(0, 40)))
        pattern = "".join(rng.choice("abcd") for _ in range(rng.randint(1, 6)))
        got = find_anagrams(source, pattern)
        want = _brute_force_anagrams(source, pattern)
        assert got == want, (source, pattern, got, want)

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
