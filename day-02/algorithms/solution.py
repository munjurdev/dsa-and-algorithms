"""
Solution for: Word-frequency analyzer capstone
Day:      day-02
Track:    algorithms
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Five small pure functions compose into an analyzer: `tokenize` lowercases
    and extracts letter/digit runs with one regex pass; `word_counts` walks
    the token list once into a dict; `top_words` guards k <= 0, sorts by
    (-count, word) and slices; `filter_words` keeps entries at or above a
    minimum length via a comprehension over a sorted copy; `summarize` chains
    tokenize -> word_counts -> top_words into (word, count) pairs.

Time Complexity:  O(n + m + u log u)   # n chars tokenising, m tokens counting, u distinct sorting
Space Complexity: O(m + u)             # token list + one counter entry per distinct word

Review Date:  2026-11-02 / 2026-11-08 / 2026-12-01
"""

from __future__ import annotations

import re


def tokenize(text: str) -> list[str]:
    """Lowercase `text` and return its letter/digit word runs in order.

    Args:
        text: raw input; may be empty, may contain punctuation.

    Returns:
        Lowercased words; punctuation and separators are dropped.
    """
    return re.findall(r"[a-z0-9]+", text.lower())


def word_counts(words: list[str]) -> dict[str, int]:
    """Return how often each word appears in `words` (one pass).

    Args:
        words: tokens, as produced by `tokenize`.

    Returns:
        A new dict mapping each distinct word to its multiplicity.
    """
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_words(counts: dict[str, int], k: int) -> list[str]:
    """Return the `k` most frequent words, ties broken alphabetically.

    Args:
        counts: a frequency map; not mutated.
        k: how many words to return; non-positive gives an empty list.

    Returns:
        Up to `k` words ordered by descending frequency.
    """
    if k <= 0:
        return []
    ranked: list[tuple[str, int]] = sorted(
        counts.items(), key=lambda entry: (-entry[1], entry[0])
    )
    return [word for word, _count in ranked[:k]]


def filter_words(counts: dict[str, int], min_length: int) -> dict[str, int]:
    """Return the entries whose word is at least `min_length` characters.

    Args:
        counts: a frequency map; not mutated.
        min_length: inclusive minimum word length to keep.

    Returns:
        A new dict with shorter words removed, keys in alphabetical order.
    """
    return {
        word: count
        for word, count in sorted(counts.items())
        if len(word) >= min_length
    }


def summarize(text: str, k: int) -> list[tuple[str, int]]:
    """Compose tokenize -> word_counts -> top_words into (word, count) pairs.

    Args:
        text: raw input to analyse.
        k: how many top words to report.

    Returns:
        The top `k` words with their counts, most frequent first.
    """
    counts: dict[str, int] = word_counts(tokenize(text))
    return [(word, counts[word]) for word in top_words(counts, k)]


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # Typical case
    text: str = "The cat sat on the mat. The cat!"
    counts: dict[str, int] = word_counts(tokenize(text))
    assert counts == {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}
    assert top_words(counts, 2) == ["the", "cat"]
    assert summarize(text, 2) == [("the", 3), ("cat", 2)]
    assert summarize(text, 2) == summarize(text, 2)  # deterministic

    # Edge cases
    assert tokenize("Hello, HELLO!") == ["hello", "hello"]  # case + punctuation
    assert word_counts([]) == {}                            # empty input
    assert top_words(counts, 0) == []                       # k = 0
    assert top_words(counts, 99) == ["the", "cat", "mat", "on", "sat"]
    assert top_words({"b": 2, "a": 2}, 2) == ["a", "b"]     # tie → alphabetical
    assert filter_words(counts, 3) == {"cat": 2, "mat": 1, "sat": 1, "the": 3}
    assert filter_words(counts, 4) == {}                    # all words shorter

    # Purity: inputs are never mutated
    tie: dict[str, int] = {"b": 2, "a": 2}
    snapshot: dict[str, int] = dict(tie)
    filter_words(tie, 1)
    top_words(tie, 1)
    assert tie == snapshot
    print("All tests passed.")


if __name__ == "__main__":
    main()
