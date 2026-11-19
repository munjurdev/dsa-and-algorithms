"""
Solution for: Valid Parentheses
Day:      day-14
Track:    dsa
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Scan the string once, keeping every unclosed opening bracket on a stack.
    A closing bracket must complete the bracket on top of the stack, so it is
    either matched (pop) or the string is invalid immediately. Opening
    brackets are pushed and never inspected until their closer arrives. At
    the end the stack must be empty: leftovers mean unclosed openers, and a
    closer against an empty stack means an opener was missing.

Time Complexity:  O(n)  # one pass; append/pop are amortized O(1), dict lookup O(1) average
Space Complexity: O(n)  # the stack holds at most the number of opening brackets

Review Date:  2026-11-20 (1 day) · 2026-11-26 (7 days) · 2026-12-19 (30 days)
"""

from __future__ import annotations

from collections import Counter

OPENERS = "([{"
CLOSERS = {")": "(", "]": "[", "}": "{"}


def is_valid(s: str) -> bool:
    """Return True iff every bracket in `s` is closed in the right order.

    Args:
        s: a string over the six bracket characters only.

    Returns:
        ``True`` for a well-formed bracket sequence, including the empty one;
        ``False`` as soon as a closing bracket mismatches or the stack is not
        empty at the end.
    """
    # --- Solution -------------------------------------------------------
    stack: list[str] = []

    for char in s:
        if char in CLOSERS:
            if not stack or stack.pop() != CLOSERS[char]:
                return False
        else:
            stack.append(char)

    return not stack


def is_valid_by_erasure(s: str) -> bool:
    """O(n^2) reference: repeatedly erase adjacent pairs until nothing changes.

    A sequence is balanced exactly when deleting every adjacent ``()``,
    ``[]``, or ``{}`` pair eventually leaves the empty string — the same
    statement as "every closer matches the most recent opener", just executed
    without a stack.
    """
    previous = None
    while previous != s:
        previous = s
        for pair in ("()", "[]", "{}"):
            s = s.replace(pair, "")
    return s == ""


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's examples
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([])") is True

    # Edge cases: empty, single opener, single closer, interleaved, nested
    assert is_valid("") is True
    assert is_valid("(") is False
    assert is_valid(")") is False
    assert is_valid("([)]") is False
    assert is_valid("{[()]}") is True
    assert is_valid("(((((((((())))))))))") is True

    # A closer that arrives after its opener was consumed
    assert is_valid("()]") is False
    assert is_valid("([)") is False

    # Maximum nesting the platform allows (10^4 characters)
    assert is_valid("(" * 5000 + ")" * 5000) is True
    assert is_valid("(" * 5000 + ")" * 4999) is False

    # Exhaustive differential check: every string of length 0..6 over all six
    # bracket characters, compared against the erase-adjacent-pairs oracle.
    alphabet = OPENERS + ")]}"
    checked = 0
    for length in range(7):
        for encoded in range(len(alphabet) ** length):
            chars: list[str] = []
            value = encoded
            for _ in range(length):
                chars.append(alphabet[value % len(alphabet)])
                value //= len(alphabet)
            candidate = "".join(chars)
            got = is_valid(candidate)
            want = is_valid_by_erasure(candidate)
            assert got is want, (candidate, got, want)
            checked += 1
    assert checked == sum(6**length for length in range(7)) == 55987

    # The count of valid strings of each even length matches the known
    # Motzkin-like totals, an independent sanity check on the oracle itself.
    counts = Counter()
    for length in range(0, 7, 2):
        for encoded in range(len(alphabet) ** length):
            chars = []
            value = encoded
            for _ in range(length):
                chars.append(alphabet[value % len(alphabet)])
                value //= len(alphabet)
            if is_valid("".join(chars)):
                counts[length] += 1
    assert counts[0] == 1
    assert counts[2] == 3
    assert counts[4] == 18

    print("All tests passed.")


if __name__ == "__main__":
    main()
