# Longest Substring Without Repeating Characters

| Field | Value |
|---|---|
| Day | `day-10` |
| Track | `dsa` |
| Topic | `09-sliding-window` — see `resources/topics/` |
| Difficulty | Medium |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/longest-substring-without-repeating-characters/ |

## Problem summary

Given a string `s`, return the length of the longest **contiguous** substring
that contains no repeated character. The answer is a length, not the substring
itself. A variable-size sliding window is the intended shape: expand right one
character at a time and, the moment the window holds a duplicate, move left
past the earlier copy.

### Input

- `s: str` — `0 <= len(s) <= 5·10⁴` on the platform, consisting of letters,
  digits, symbols, and spaces (this implementation also handles any Unicode).
- Being total: an empty string is a valid input and returns `0`.

### Output

- `int` — the largest `r - l + 1` over all windows `s[l:r + 1]` whose
  characters are pairwise distinct.

## Approach

1. Keep `last_seen: char → index of its most recent occurrence`, `left = 0`
   (the window's inclusive left edge), and `best = 0`.
2. For each `right` from `0` to `n - 1`:
   - look up `previous = last_seen.get(s[right])`;
   - if `previous` exists **and** `previous >= left`, the character is already
     inside the window, so set `left = previous + 1`;
   - write `last_seen[s[right]] = right`;
   - set `best = max(best, right - left + 1)`.
3. Return `best`.

The window is never rebuilt: `left` only moves forward, the map only stores the
latest index per character, and the length is measured before the next
character arrives.

## Why this approach works

**Invariant (one sentence):** after processing index `right`, the window
`s[left : right + 1]` has no duplicate character, and `left` is the smallest
index for which that is true.

*It stays duplicate-free.* When `s[right]` is new to the window
(`previous` is missing or `< left`), nothing in the window repeats, so the
extended window is still valid. When it is already inside, the only duplicates
created involve `s[right]` and its previous occurrence at `previous`, so
dropping everything up to and including `previous` — `left = previous + 1` —
removes every copy of that character and leaves no other duplicate, because the
window was valid immediately before.

*It is the longest window ending at `right`.* Any valid window ending at
`right` cannot start at or before `previous`, since `s[previous] == s[right]`
would repeat. `left = previous + 1` is therefore the earliest legal start, and
the window is the longest valid one ending here.

*The maximum over ends is the answer.* Every substring ends at exactly one
`right`, so taking the maximum valid length over all `right` visits every
candidate. Measuring after the update — and never letting `left` move backwards
— is what makes the `"abba"` case return `2`: at the last `a`,
`previous = 0 < left = 2`, so `left` stays at `2` instead of rewinding.

Each index enters the window once (as `right`) and can be passed by `left` at
most once, which is where the linear time comes from.

## Complexity

- **Time:** O(n) — one pass over `s`; each step does one dictionary lookup and
  at most one dictionary write, and `left` advances at most `n` times in total
  because it never decreases.
- **Space:** O(min(n, σ)) — one integer per **distinct** character currently
  seen, where `σ` is the alphabet size (at most `n` distinct characters).

## Edge cases

- `""` → `0`; `"a"` → `1`; `" "` → `1` (a space is an ordinary character).
- All identical: `"bbbbb"` → `1`.
- All distinct: `"abcdef"` → `6`.
- `"abba"` → `2` — the `left` pointer must not rewind to `previous + 1 = 1`.
- `"dvdf"` → `3` (`"vdf"`), not `2` — the answer may start *inside* the
  dropped prefix.
- `"pwwkew"` → `3` (`"wke"`); the longest **substring** is not a subsequence,
  so `"pwke"` does not count.
- Repeated characters far apart: `"tmmzuxt"` → `5` (`"mzuxt"`), including a
  repeat of the very first character.
- Non-ASCII and multi-byte text: `"বাংলা"` → `4` — Python indexes code
  points, so `"া"` repeating twice is detected normally; `"🙂🙂🙃"` → `2`.
- Digits and punctuation: `"a1b2c3!@#"` → `9`; `"???!!"` → `2`.
- Platform maximum (`5·10⁴` characters) is a single pass; no recursion, so no
  stack-depth concern.
- Input string is immutable and never modified.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `"abcabcbb"` | `3` | the statement's example (`"abc"`) |
| `"bbbbb"` | `1` | one repeated character |
| `"pwwkew"` | `3` | `"wke"`, not the subsequence `"pwke"` |
| `""` | `0` | empty input |
| `" "` | `1` | whitespace counts |
| `"abba"` | `2` | `left` must not move backwards |
| `"dvdf"` | `3` | best window starts inside the prefix |
| `"tmmzuxt"` | `5` | repeat of the first character |
| `"abcdef"` | `6` | whole string distinct |
| `"বাংলা"` | `4` | `"া"` repeats; non-ASCII is indexed normally |
| `"🙂🙂🙃"` | `2` | multi-byte characters |
| `"ab c d e"` | `4` | spaces are characters (`"ab c"`) |
| `"a1b2c3!@#"` | `9` | digits and punctuation |
| every string of length 0–7 over `"abc"` | equals brute force **and** a set-based shrink loop | exhaustive differential check |
| 500 random strings of length 0–60 over `"abcd"` | equals both oracles | randomized differential check |
| 200 random strings of length 0–40 over `a…z` | equals the set-based oracle | wider alphabet |

## What I learned

- **Pattern:** for "longest window with property X", keep the window valid by
  moving `left` to the *first legal start* rather than shrinking one step at a
  time — with last-seen indices that jump is exact and still `O(n)` total.
- **Pitfall:** using `left = previous + 1` unconditionally rewinds the window
  on a stale occurrence (`"abba"` → `3`). The guard `previous >= left` is what
  keeps `left` monotone.
- **Differently next time:** write the invariant down first ("window is
  duplicate-free and left is minimal"), then check the two obligations — no
  duplicates after the move, and no valid window could start earlier. Both
  proofs are one line each once the invariant is stated.

**Review date:** 2026-11-12 (1 day) · 2026-11-18 (7 days) · 2026-12-11 (30 days)
