# Minimum Window Substring

| Field | Value |
|---|---|
| Day | `day-11` |
| Track | `dsa` |
| Topic | `09-sliding-window` — see `resources/topics/` |
| Difficulty | Hard |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/minimum-window-substring/ |

## Problem summary

Given strings `s` and `t`, return the shortest **contiguous** substring of `s`
that contains every character of `t`, counting repetitions — `t = "aa"` needs
two `a`s, not one. If no such window exists the answer is the empty string.
This is the variable-size window in its hardest form: validity is "all
requirements met", so the window expands until it covers `t` and then shrinks
as far as it can without losing coverage.

### Input

- `s: str` — `1 <= len(s) <= 10⁵` on the platform, letters and digits (this
  implementation also handles any Unicode).
- `t: str` — `1 <= len(t) <= 10⁵` on the platform; may repeat characters and
  may be longer than `s`.
- Being total: an empty `t` or an empty `s` returns `""` instead of raising.

### Output

- `str` — a shortest substring `s[i:j]` with `Counter(s[i:j]) >= Counter(t)`,
  or `""` when none exists. Ties are all equally valid; this implementation
  returns the leftmost shortest window.

## Approach

1. Build `need = Counter(t)` and set `missing = len(t)` — the number of
   required characters the window does not yet cover.
2. Expand `right` across `s`. For each character:
   - if `need[char] > 0` the window still owed one of these, so `missing -= 1`;
   - then `need[char] -= 1`. Negative counts mean *surplus*: more copies than
     required.
3. While `missing == 0` the window is valid:
   - compare its length with the best so far and remember the start if shorter;
   - release the left character (`need[leaving] += 1`); if that pushes its
     count back above `0`, a requirement is now uncovered — `missing += 1` —
     and the `while` stops;
   - advance `left`.
4. Return the best slice, or `""` if the best length was never set.

The window is never rebuilt: `left` and `right` only move forward, and the
count map is the entire state.

## Why this approach works

**Invariant (one sentence):** `missing == 0` exactly when the window
`s[left:right + 1]` contains at least `Counter(t)` of every character, and the
`while` loop leaves `left` at the smallest index for which the window ending at
`right` is still valid.

*The counts are exact.* `need[c]` starts at the required count and is
decremented once per window occurrence. So `need[c] > 0` means "still short by
that many", `need[c] == 0` means "exactly satisfied", and `need[c] < 0` means
"surplus by that many". Subtracting `1` from `missing` only on `need[c] > 0`
therefore counts requirements, not occurrences — which is precisely why
repeated required characters work (`t = "aab"` needs two `a`s).

*Shrinking stops at the right place.* Removing `s[left]` increases
`need[s[left]]` by one. If it becomes positive, that character was satisfied
exactly (not in surplus), so the window is now short by one and invalid:
`missing > 0` and the loop ends. If it stays `<= 0` the character was surplus,
so the shorter window still covers `t` and shrinking continues. Hence the first
window length recorded in each `while` run is achieved after discarding only
surplus characters.

*No shorter window is missed.* Every window is defined by its right end. For
each `right` the algorithm considers the shortest valid window ending there —
the one reached after shedding all possible surplus from the left — and a
shorter valid window ending anywhere must start after that `left`, so it would
already have been recorded at an earlier `right`. Taking the minimum over all
right ends therefore yields the global minimum.

*It stays linear.* `right` visits each index once, and `left` only increases,
so across the whole scan at most `n` left characters are released.

## Complexity

- **Time:** O(n + m) — `Counter(t)` costs `O(m)`; the scan touches each `s`
  character once as `right` and at most once as `left`, with `O(1)` map work
  per step.
- **Space:** O(σ) — one integer per distinct character of `t`, `σ` being the
  alphabet size (bounded by 52 for letters, at most `min(m, n)` in general);
  the answer is a slice, not a search structure.

## Edge cases

- `t == ""` → `""` (nothing to cover, no meaningful window).
- `s == ""` or `len(t) > len(s)` → `""` immediately.
- `s == "a", t == "a"` → `"a"`; `s == "a", t == "aa"` → `""`.
- Repeated requirements: `s = "aa", t = "aa"` → `"aa"`;
  `s = "ab", t = "aa"` → `""`; `s = "aabc", t = "aab"` → `"aab"`.
- Surplus inside the window: `s = "abbbbbcdd", t = "abcdd"` →
  `"abbbbbcdd"` (the surplus `b`s are unavoidable).
- Window pinned to an end: `"abcxyz"`/`"abc"` → `"abc"` (left end);
  `"xyzabc"`/`"abc"` → `"abc"` (right end).
- Shortest window is not the first `c` extended to the next `a` and `e`:
  `"cabwefgewcwaefgcf"`/`"cae"` → `"cwae"`, because a later `a` and `e` lie
  closer to that `c` — this defeats "scan for the first `c` and extend".
- All characters identical: `s = "bbbbbbbbbb", t = "b"` → `"b"`.
- `len(s) == len(t)`: at most one candidate; returned only if it covers `t`.
- Non-ASCII text works because Python counts code points; no byte assumptions.
- The inputs are never mutated; the result is a slice of `s`.
- Platform maximum (`10⁵` characters each) is one linear scan; no recursion.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `"ADOBECODEBANC"`, `"ABC"` | `"BANC"` | the statement's example |
| `"a"`, `"a"` | `"a"` | single character |
| `"a"`, `"aa"` | `""` | repetition cannot be satisfied |
| `"abc"`, `""` | `""` | empty target |
| `""`, `"a"` | `""` | empty source |
| `"ab"`, `"abc"` | `""` | target longer than source |
| `"aa"`, `"aa"` | `"aa"` | repeated requirement satisfied exactly |
| `"ab"`, `"aa"` | `""` | repeated requirement unsatisfiable |
| `"aabc"`, `"aab"` | `"aab"` | must not stop at the first `a` |
| `"bba"`, `"ab"` | `"ba"` | answer starts at index 1 |
| `"aaflslflsldkalskaaa"`, `"aaa"` | `"aaa"` | many scattered occurrences |
| `"aaaaaaaaaaaabbbbbcdd"`, `"abcdd"` | `"abbbbbcdd"` | surplus `b`s are unavoidable |
| `"xyzabcxyz"`, `"abc"` | `"abc"` | interior window |
| `"abcxyz"`, `"abc"` | `"abc"` | window at the start |
| `"xyzabc"`, `"abc"` | `"abc"` | window at the end |
| `"cabwefgewcwaefgcf"`, `"cae"` | `"cwae"` | shortest window is non-obvious |
| `"bbbbbbbbbb"`, `"b"` | `"b"` | single needed character |
| every `s` of length 0–6 and `t` of length 0–3 over `"ab"` | same **length** as an `O(n²)` brute force | exhaustive differential check, repeated characters included |
| 300 random `s` (length 0–25) and `t` (length 0–4) over `"abc"` | same length as the brute force, and the answer really covers `t` | randomized differential check |

## What I learned

- **Pattern:** "shortest window covering a multiset" is the expand-until-valid,
  shrink-while-valid window — the counterpart of the "longest window with no
  violation" shape from Day 10, and the two differ exactly in which condition
  drives shrinking.
- **Pitfall:** counting occurrences instead of *requirements* (e.g. clearing a
  boolean "seen" flag) silently passes `"ADOBECODEBANC"` and fails every
  repeated-character case like `t = "aa"`. Letting counts go negative is what
  makes surplus droppable in `O(1)`.
- **Differently next time:** write the `missing`/surplus bookkeeping down as an
  invariant before touching the code, and test against a brute force over the
  two-letter alphabet — every repetition bug shows up there within a second.

**Review date:** 2026-11-16 (1 day) · 2026-11-22 (7 days) · 2026-12-15 (30 days)
