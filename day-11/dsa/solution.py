"""
Solution for: Minimum Window Substring
Day:      day-11
Track:    dsa
Difficulty: Hard

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Count how many of each character the target needs, then slide a window to
    the right. Each incoming character reduces the number of still-missing
    requirements (counts may go negative, meaning "surplus"). The moment
    nothing is missing the window is valid, so record it if it is the shortest
    so far and shrink from the left until one requirement becomes missing
    again. Surplus characters are dropped for free, which is what keeps the
    scan linear.

Time Complexity:  O(n + m)  # each of the n characters enters and leaves the window at most once
Space Complexity: O(σ)      # need-count per distinct character, σ = alphabet size (≤ 52 here)
"""

from __future__ import annotations

import random
from collections import Counter


def min_window(s: str, t: str) -> str:
    """Return the shortest substring of `s` containing every character of `t`.

    Args:
        s: the string to search in; may be empty.
        t: the required multiset; repetitions mean "at least this many".

    Returns:
        The shortest contiguous substring of `s` whose character counts cover
        `t`, or `""` when no such substring exists. When several windows tie,
        the leftmost one is returned (they are all equally short).
    """
    # --- Solution -------------------------------------------------------
    if not t or not s or len(t) > len(s):
        return ""

    need = Counter(t)
    missing = len(t)  # required characters not yet covered by the window
    best_start = 0
    best_len = len(s) + 1
    left = 0

    for right, char in enumerate(s):
        if need[char] > 0:
            # This occurrence is still required, not surplus.
            missing -= 1
        need[char] -= 1

        while missing == 0:
            # Every requirement is covered: try to shrink from the left.
            window_len = right - left + 1
            if window_len < best_len:
                best_start, best_len = left, window_len
            leaving = s[left]
            need[leaving] += 1
            if need[leaving] > 0:
                # The window no longer covers `leaving`; stop shrinking.
                missing += 1
            left += 1

    if best_len > len(s):
        return ""
    return s[best_start : best_start + best_len]


def _covers(window: str, target: str) -> bool:
    """True when `window` contains at least the multiset of `target`."""
    return all(count <= 0 for count in (Counter(target) - Counter(window)).values())


def _brute_force_length(s: str, t: str) -> int:
    """O(n^2) reference: shortest substring that covers `t` (0 if none)."""
    if not t:
        return 0
    best = 0
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if _covers(piece, t) and (best == 0 or len(piece) < best):
                best = len(piece)
    return best


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's examples
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""

    # Nothing to find / nothing to look in
    assert min_window("abc", "") == ""
    assert min_window("", "a") == ""
    assert min_window("ab", "abc") == ""

    # Repeated required characters are the whole difficulty of this problem
    assert min_window("aa", "aa") == "aa"
    assert min_window("ab", "aa") == ""
    assert min_window("aabc", "aab") == "aab"
    assert min_window("bba", "ab") == "ba"
    assert min_window("aaflslflsldkalskaaa", "aaa") == "aaa"
    assert min_window("aaaaaaaaaaaabbbbbcdd", "abcdd") == "abbbbbcdd"

    # Surplus characters inside the window, and window at either end
    assert min_window("xyzabcxyz", "abc") == "abc"
    assert min_window("abcxyz", "abc") == "abc"
    assert min_window("xyzabc", "abc") == "abc"
    assert min_window("cabwefgewcwaefgcf", "cae") == "cwae"

    # Single repeated target character in a longer string
    assert min_window("bbbbbbbbbb", "b") == "b"

    # The answer must cover `t` and be as short as the oracle says
    for size in range(0, 7):
        for source in _strings_of("ab", size):
            for t_size in range(0, 4):
                for target in _strings_of("ab", t_size):
                    got = min_window(source, target)
                    want = _brute_force_length(source, target)
                    assert len(got) == want, (source, target, got, want)
                    if want:
                        assert _covers(got, target), (source, target, got)
                        assert got in source, (source, target, got)

    # Randomized differential check over a slightly wider alphabet
    rng = random.Random(20261115)
    for _ in range(300):
        source = "".join(rng.choice("abc") for _ in range(rng.randint(0, 25)))
        target = "".join(rng.choice("abc") for _ in range(rng.randint(0, 4)))
        got = min_window(source, target)
        want = _brute_force_length(source, target)
        assert len(got) == want, (source, target, got, want)
        if want:
            assert _covers(got, target), (source, target, got)

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
