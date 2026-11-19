# Valid Parentheses

| Field | Value |
|---|---|
| Day | `day-14` |
| Track | `dsa` |
| Topic | `12-stack` — see `resources/topics/` |
| Difficulty | Easy |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/valid-parentheses/ |

## Problem summary

Given a string made only of the characters `()[]{}`, decide whether every
bracket is closed by the matching kind and in the correct nesting order. The
question is not "are the counts equal" — `([)]` has equal counts and is
invalid — but "does every closer finish the most recently opened, still-open
bracket". That last-opened-first requirement is exactly LIFO, so the string
is validated one character at a time with a stack.

### Input

- `s: str` — 1 to 10⁴ characters, each one of `(`, `)`, `[`, `]`, `{`, `}`.
  (The empty string is treated as valid here, matching the recursive
  definition; the platform's constraint excludes it, the code should not care.)

### Output

- `bool` — `True` if the sequence is well-formed, `False` otherwise.

## Approach

1. Keep `stack: list[str]` for the opening brackets seen so far.
2. For each character:
   - if it is a **closer**, it must match the bracket on top:
     - empty stack → `False` (a closer with no opener);
     - `stack.pop() != match[closer]` → `False` (wrong kind or wrong nesting);
   - otherwise it is an **opener** → `stack.append(char)`.
3. After the scan, return `stack == []`: a non-empty stack means openers were
   never closed.

The closer→opener table (`{")": "(", "]": "[", "}": "{"}`) keeps the check to
one dictionary lookup instead of a chain of `if`/`elif`.

## Why this approach works

**Invariant (one sentence):** after processing a prefix, the stack holds
exactly the brackets that were opened in that prefix and not yet closed, in
opening order bottom-to-top — so its top is the only bracket the next closer
is allowed to close.

*Every closer is checked against the only candidate.* Nesting forbids closing
an outer bracket while an inner one is open, and the stack's top is precisely
that innermost unclosed opener; comparing against anything else would accept
`([)]`.

*The end condition is exact.* Each opener is pushed once and popped at most
once, so an opener that survived to the end was never closed — and one that
was popped early was closed by a matching closer. Hence "stack empty" is
equivalent to "every bracket was closed correctly", not just to "counts
match".

## Complexity

- **Time:** O(n) — one pass over the string; `list.append` is amortized O(1)
  (the occasional resize copies, but a doubling table makes the average
  constant), `list.pop()` is O(1), and the dictionary lookup is O(1) average.
  n characters → O(n) total, not O(n) per character.
- **Space:** O(n) — the stack stores at most every opening bracket, which is
  the worst case for input like `"(((("` or fully nested `"((()))"`. No other
  auxiliary structure is used.

## Edge cases

- `""` → `True` (nothing to close); `"("` and `")"` → `False`.
- `"()[]{}"` → `True`; `"(]"` → `False` (wrong kind at depth 1).
- `"([)]"` → `False` even though all counts are equal — the nesting check is
  what rejects it.
- `"([)]"`-style crossing is caught by the top-of-stack comparison, not by
  counting: counting is the classic wrong solution.
- Closer-first strings (`")("`, `"]"`) fail on `not stack` before any pop, so
  no `IndexError` can escape.
- Leftover openers (`"(()"`, `"([{"`) fail at the final empty-stack test.
- Deep nesting (`"(" * 5000 + ")" * 5000`) is fine: the stack is a list, not
  Python call frames, so the platform's 10⁴ limit does not hit a recursion
  limit.
- Input is guaranteed to contain only the six bracket characters, so the
  `else` branch is safe to treat every non-closer as an opener; a broader
  alphabet would need an explicit `if char in OPENERS` guard.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `"()"` | `True` | minimum balanced pair |
| `"()[]{}"` | `True` | all three kinds side by side |
| `"(]"` | `False` | wrong closer kind |
| `"([])"` | `True` | proper nesting |
| `""` | `True` | empty sequence is vacuously valid |
| `"("` | `False` | opener never closed |
| `")"` | `False` | closer with no opener |
| `"([)]"` | `False` | equal counts, wrong order |
| `"()]"` | `False` | closer after the pair is finished |
| `"([)"` | `False` | inner closer closes the wrong bracket |
| `"{[()]}"` | `True` | three-deep nesting |
| `"(((((((((())))))))))"` | `True` | repeated identical brackets |
| `"(" * 5000 + ")" * 5000` | `True` | platform's maximum length, deep stack |
| `"(" * 5000 + ")" * 4999` | `False` | one opener left over at maximum length |
| all 55,987 strings of length 0–6 over the six characters | matches erase-adjacent-pairs oracle | exhaustive differential check |
| valid counts for lengths 0/2/4 | 1 / 3 / 18 | independent check on the oracle, not just on the solution |

## What I learned

- **Pattern:** a stack turns "the most recent unfinished thing" into an O(1)
  lookup. Bracket matching, expression evaluation, and undo all read the same
  way: push work, resolve it when the input supplies its answer.
- **Pitfall:** counting closers is the tempting wrong answer because the
  examples mostly pass; `"([)]"` is the one-line counterexample, and the stack
  invariant explains why counting cannot work — it discards order.
- **Differently next time:** write the erase-adjacent-pairs oracle first. It
  is a different algorithm (text rewriting, no stack), so agreement between
  the two is real evidence, whereas checking against remembered outputs is
  not.

**Review date:** 2026-11-20 (1 day) · 2026-11-26 (7 days) · 2026-12-19 (30 days)
