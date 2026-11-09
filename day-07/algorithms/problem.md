# Weekly Checkpoint 01 — Timed Re-Solve of 4 Problems from Days 01–06

| Field | Value |
|---|---|
| Day | `day-07` |
| Track | `algorithms` |
| Topic | `06-hashing` (checkpoint — material from `00`–`05`) |
| Difficulty | Easy |
| Platform | Other (self-made checkpoint exercise) |
| URL | _none — the four problems are named below_ |

## Problem summary

The Day 007 checkpoint from [`ROADMAP.md`](../../ROADMAP.md): rebuild four
previously solved problems from blank files, **closed notes**, and prove each
one still passes. The four chosen span the phases behind Day 07 — frequency
maps (`Valid Anagram`), single-pass running state (`Maximum Subarray`), matrix
boundaries (`Spiral Matrix`), and sort-then-scan (`Merge Intervals`). The
completion criterion is 4 of the four re-derived without opening the old code;
duplicating the old file would not count.

`day-07/algorithms/solution.py` holds all four functions plus a reference
implementation for each, so every re-solve is checked by a *different*
algorithm rather than by remembered expected outputs.

| # | Problem | From | Function |
|---|---|---|---|
| 1 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | `day-02/dsa` | `is_anagram` |
| 2 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | `day-04/algorithms` | `max_subarray` |
| 3 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | `day-05/algorithms` | `spiral_order` |
| 4 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | `day-06/dsa` | `merge_intervals` |

### Input

- `is_anagram(s: str, t: str)` — any two strings, case-sensitive, possibly
  empty.
- `max_subarray(nums: list[int])` — at least one integer; negatives allowed.
- `spiral_order(matrix: list[list[int]])` — rectangular `m × n` grid;
  `[]` is empty, `[[]]` and ragged rows are malformed.
- `merge_intervals(intervals: list[list[int]])` — `[start, end]` pairs in any
  order with `start <= end`, possibly nested, touching, or duplicated.

### Output

- `bool`; `int`; `list[int]` (the `m · n` values in spiral order); and
  `list[list[int]]` (disjoint intervals sorted by start). Malformed or
  impossible input raises `ValueError` in all three total functions.

## Approach

1. **Valid Anagram** — length guard first; count `s` into a dict, then decrement
   while scanning `t`. A missing key or a zero count means a surplus character.
2. **Maximum Subarray** — Kadane: `best_ending_here = max(value,
   best_ending_here + value)`, updating `best` each step, both seeded from
   `nums[0]`.
3. **Spiral Matrix** — validate rectangularity, then peel borders with four
   boundaries `top/bottom/left/right`; the bottom and left edges each get their
   own guard so a one-row or one-column grid cannot emit a cell twice.
4. **Merge Intervals** — validate every pair, sort by start, then close the
   current group when `start > current_end`; otherwise extend with
   `current_end = max(current_end, end)`.

Each function is then tested against its own reference: `sorted()` for the
anagram, every-slice brute force for Kadane, a direction-walk simulation for
the spiral, and a pairwise fixed-point merge plus a union-coverage check for
the intervals.

## Why this approach works

- **Anagram:** two strings are anagrams exactly when their character-count maps
  are equal; decrementing computes the difference, and a negative count proves
  a surplus (equal lengths rule out a deficit). `sorted()` is an independent
  oracle because it compares content without any counting.
- **Kadane:** every best subarray ending at index `i` either is `nums[i]` alone
  or extends the best subarray ending at `i - 1` — those are the only two
  cases, and `max` picks the better one. Seeding from `nums[0]` forbids the
  empty sum, which is what makes the all-negative case return its largest
  element.
- **Spiral:** each loop iteration consumes the current rectangle's border
  clockwise and shrinks the rectangle, so the emitted prefix is always exactly
  the spiral so far. The two guards are the statement "a row/column still
  remains"; without them `1 × n` and `n × 1` boards re-emit the border just
  taken.
- **Merge Intervals:** after sorting by start, the next interval merges with
  the open group iff `start <= current_end`; if `start > current_end` there is
  a real gap, and every later interval starts even further right, so the group
  is finished. `max` on the end keeps a nested interval from shrinking the
  group, and `<=` (not `<`) is what merges touching intervals.

## Complexity

| Function | Time | Space | Why |
|---|---|---|---|
| `is_anagram` | O(n) | O(k) | one count pass, one decrement pass; `k` distinct characters |
| `max_subarray` | O(n) | O(1) | one pass, two integers of state |
| `spiral_order` | O(m·n) | O(1) | every cell appended once; four boundary indices |
| `merge_intervals` | O(n log n) | O(n) | the sort dominates; the scan is linear |

## Edge cases

- **Anagram:** `""` vs `""` → `True`; `"a"` vs `"ab"` → `False` from the length
  guard; `"aabb"` vs `"abbb"` → `False` (equal *sets*, different counts);
  `"Anagram"` vs `"nagaram"` → `False` (case-sensitive).
- **Kadane:** empty input → `ValueError`; `[-3, -1, -2]` → `-1` (never the
  empty sum `0`); `[0, -1]` → `0`; single element returns itself.
- **Spiral:** `[]` → `[]`; `[[]]` and `[[1, 2], [3]]` → `ValueError`; `1 × n`,
  `n × 1`, and `1 × 1` each emit their cells exactly once; `2 × 2` ends on a
  complete ring; `2 × 3` and `3 × 2` leave a degenerate remainder that the
  guards handle.
- **Intervals:** `[]` → `[]`; a single interval is returned unchanged;
  touching `[1, 4], [4, 5]` → `[1, 5]`; nested `[1, 4], [2, 3]` → `[1, 4]`;
  duplicates collapse; `[1, 2], [3, 4]` stays two intervals; negatives work;
  `[[]]`, `[[1]]`, `[[3, 1]]`, `[[1, 2, 3]]` → `ValueError`.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `("anagram", "nagaram")` | `True` | typical anagram |
| `("aabb", "abbb")` | `False` | equal sets, different counts |
| `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` | `6` | statement's Kadane example |
| `[-3, -1, -2]` | `-1` | all-negative trap |
| `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` | `[1,2,3,6,9,8,7,4,5]` | square spiral |
| `[[1, 2, 3]]`, `[[1], [2], [3]]` | `[1,2,3]` | one row / one column guards |
| `[[1, 3], [8, 10], [2, 6], [15, 18]]` | `[[1,6],[8,10],[15,18]]` | sort then scan |
| `[[1, 4], [4, 5]]` | `[[1, 5]]` | touching intervals merge |
| `[[1, 4], [2, 3]]` | `[[1, 4]]` | nesting must not shrink the group |
| 300 random string pairs | equals `sorted() = sorted()` | anagram oracle |
| 300 random arrays | equals brute force | Kadane differential |
| every shape `1…6 × 1…6` | equals the direction-walk spiral; same multiset of cells | spiral differential |
| 300 random interval lists | equals pairwise fixed point and covers the same points | interval differential |

## What I learned

- **Pattern:** the four re-solves map onto four different running states — a
  frequency map, two Kadane registers, four matrix boundaries, one open
  interval group. Naming today's state out loud is what makes the re-derivation
  fast rather than memorised.
- **Pitfall:** the two bugs that came back under time pressure were both
  boundary conditions, not ideas: Kadane seeded at `0` instead of `nums[0]`
  would answer `0` for an all-negative array, and the spiral needs its own
  `top <= bottom` / `left <= right` guards for single-row and single-column
  grids. A checkpoint is exactly where those resurface.
- **Differently next time:** keep each reference implementation next to the
  re-solve from the start. Checking a re-derivation against a remembered
  expected list tests memory, while checking it against a different algorithm
  tests understanding.

**Review date:** 2026-11-10 (1 day) · 2026-11-16 (7 days) · 2026-12-09 (30 days)
