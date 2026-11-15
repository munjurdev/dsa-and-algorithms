# Find All Anagrams in a String

| Field | Value |
|---|---|
| Day | `day-11` |
| Track | `algorithms` |
| Topic | `09-sliding-window` (fixed-size window + frequency map) — see `resources/topics/` |
| Difficulty | Medium |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/find-all-anagrams-in-a-string/ |

## Problem summary

Given strings `s` and `p`, return the start index of every substring of `s`
that is an **anagram** of `p` — same characters, same multiplicities, any
order. Because every anagram has exactly `len(p)` characters, all candidates
are windows of one fixed width, so one slide with a running frequency map
answers the whole question.

### Input

- `s: str` — `1 <= len(s) <= 3·10⁴` on the platform, lowercase English
  letters (this implementation handles any Unicode).
- `p: str` — `1 <= len(p) <= 3·10⁴` on the platform; may repeat characters
  and may be longer than `s`.
- This implementation is total: an empty `p` raises `ValueError`, since an
  empty pattern would trivially match at every index.

### Output

- `list[int]` — every index `i` with `sorted(s[i:i + len(p)]) == sorted(p)`,
  in ascending order; `[]` when there is none.

## Approach

1. Reject an empty `p`; if `len(p) > len(s)` return `[]`.
2. `need = Counter(p)` and an empty `window` map; `width = len(p)`.
3. For each `right` in `0..n-1`:
   - add `s[right]` to `window`;
   - once `right >= width`, remove `s[right - width]` from `window` (delete the
     key when its count hits zero, so the maps compare cleanly);
   - once `right >= width - 1`, the window holds exactly `width` characters;
     if `window == need`, append `right - width + 1`.
4. Return the collected indices.

No window is re-counted: each step adds one character and removes at most one.

## Why this approach works

**Invariant (one sentence):** after processing `right`, `window` is exactly
the multiset of `s[max(0, right - width + 1) : right + 1]` — the last `width`
characters seen, or everything seen if fewer than `width` have arrived.

*The update is exact.* Adding the entering character and subtracting the one
`width` positions back leaves the multiset of the newest `width` characters,
which is the invariant shifted one step. Deleting zero-count keys keeps the
map equal to a fresh `Counter` of the window, so a plain `==` comparison is a
correct multiset comparison rather than a comparison of stale keys.

*Equality is the anagram test.* Two strings are anagrams exactly when their
character multisets are equal, and `Counter` equality compares multisets. So
`window == need` at a full-width window is iff `s[right - width + 1:right + 1]`
is an anagram of `p` — no sorting required.

*Every candidate is visited once.* A length-`width` substring is identified by
its right end, and each `right >= width - 1` produces exactly one such window,
so all `n - width + 1` candidates are tested, in ascending order of start index.

## Complexity

- **Time:** O(n) — one pass with `O(1)` map work per step: at most one insert,
  one decrement, and one `Counter` equality over an alphabet of fixed size (26
  lowercase letters on the platform, `σ` in general).
- **Space:** O(σ) — two count maps over the alphabet (at most `width` distinct
  keys), plus the `O(n)` output list, which is required by the return type.

## Edge cases

- `p == ""` → `ValueError` (an empty pattern is a vacuous match everywhere).
- `len(p) > len(s)` → `[]`; `s == ""` → `[]`.
- `len(p) == len(s)` → either `[0]` or `[]`.
- `len(p) == 1` → every index whose character equals `p`.
- All identical: `s = "aaaa", p = "aa"` → `[0, 1, 2]` (every window matches).
- Overlapping matches: `s = "abababab", p = "abab"` → `[0, 1, 2, 3, 4]`.
- Repeated pattern characters: `s = "baaab", p = "aab"` → `[0, 2]`;
  `s = "aabb", p = "aab"` → `[0]`.
- No match at all: `s = "abcdef", p = "gh"` → `[]`.
- Pattern not present as a substring but present as scattered letters: handled
  correctly because only windows are counted, never the whole string.
- Duplicate indices cannot occur: at most one window per right end.
- The inputs are not mutated; the result list is newly built.
- Non-ASCII text works because characters are counted as code points.
- Platform maximum (`3·10⁴` each) is one linear scan; no recursion, no sorting.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `"cbaebabacd"`, `"abc"` | `[0, 6]` | the statement's example |
| `"abab"`, `"ab"` | `[0, 1, 2]` | the statement's second example, overlapping |
| `"aaaa"`, `"aa"` | `[0, 1, 2]` | every window matches |
| `"abcdef"`, `"gh"` | `[]` | characters never appear |
| `"ab"`, `"abc"` | `[]` | pattern longer than source |
| `""`, `"a"` | `[]` | empty source |
| `"abc"`, `"a"` | `[0]` | single-character pattern |
| `"abc"`, `"bca"` | `[0]` | the whole string is an anagram |
| `"abcabc"`, `"abc"` | `[0, 1, 2, 3]` | overlapping rotations all count |
| `"aabb"`, `"aab"` | `[0]` | multiplicities must match, not just letters |
| `"aa"`, `"aaa"` | `[]` | pattern too long for its letters |
| `"baaab"`, `"aab"` | `[0, 2]` | repeated letters, non-adjacent matches |
| `"abababab"`, `"abab"` | `[0, 1, 2, 3, 4]` | heavy overlap |
| `"বাংলা"`, `"বা"` | `[0]` | non-ASCII characters |
| `"abc"`, `""` | `ValueError` | empty pattern rejected |
| every `s` of length 0–5 and non-empty `p` of length 1–3 over `"ab"` | equals the sorted-window brute force | exhaustive differential check |
| 500 random `s` (length 0–40) and `p` (length 1–6) over `"abcd"` | equals the brute force | randomized differential check |

## What I learned

- **Pattern:** a fixed-width window over a frequency map turns "all anagrams"
  into "all windows whose counter equals the pattern's counter" — the same
  sliding-sum idea as Day 10's averages, with counts instead of sums.
- **Pitfall:** leaving zero-count keys in `window` does not break `Counter`
  equality, but comparing `dict`s or hand-written loops does; deleting the key
  on zero keeps the equality test honest and the map small.
- **Differently next time:** state the window's exact contents in the
  invariant (`last width characters seen`) before coding; the early-return and
  the `right >= width - 1` guard then follow mechanically instead of being
  guessed — my first draft asserted a wrong expected value for `"abcabc"` and
  the brute-force check would have caught it instantly.

**Review date:** 2026-11-16 (1 day) · 2026-11-22 (7 days) · 2026-12-15 (30 days)
