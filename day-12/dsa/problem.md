# Search in Rotated Sorted Array

| Field | Value |
|---|---|
| Day | `day-12` |
| Track | `dsa` |
| Topic | `10-binary-search` — see `resources/topics/` |
| Difficulty | Medium |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/search-in-rotated-sorted-array/ |

## Problem summary

A strictly increasing array was rotated at some unknown pivot (`[0,1,2,4,5,6,7]`
might arrive as `[4,5,6,7,0,1,2]`). Find the index of a target value in
`O(log n)`, or `-1` when it is absent. Ordinary binary search cannot decide by
comparing `nums[mid]` with the target alone, because a "smaller" value can sit
on either side of the midpoint; the extra information is that **one of the two
halves around `mid` is always sorted**, and that half can be range-tested.

### Input

- `nums: list[int]` — `0 <= len(nums) <= 5000` on the platform, all values
  distinct, ascending before the rotation; may be empty here.
- `target: int` — any integer, including values outside the array's range.
- Precondition: `nums` is a rotation of a strictly increasing array (the
  platform guarantees it; this implementation assumes it, as the statement does).

### Output

- `int` — the index `i` with `nums[i] == target`, or `-1` if no such index.

## Approach

1. `lo, hi = 0, len(nums) - 1`; loop while `lo <= hi`.
2. `mid = (lo + hi) // 2`; return `mid` if `nums[mid] == target`.
3. If `nums[lo] <= nums[mid]`, the left half `nums[lo:mid + 1]` is sorted:
   - target inside `[nums[lo], nums[mid])` → `hi = mid - 1`;
   - otherwise the target must be in the right half → `lo = mid + 1`.
4. Otherwise the rotation lies in the left half, so `nums[mid:hi + 1]` is
   sorted:
   - target inside `(nums[mid], nums[hi]]` → `lo = mid + 1`;
   - otherwise → `hi = mid - 1`.
5. Falling out of the loop means the interval is empty: return `-1`.

The range checks use the *sorted* half's endpoints, never the rotated half's.

## Why this approach works

**Invariant (one sentence):** every iteration keeps `target`, if present, inside
`nums[lo:hi + 1]`, and halves that interval.

*At least one half is sorted.* A single rotation cuts a sorted array into two
ascending runs. The midpoint lies in one run, and the interval `[lo, hi]`
contains at most one "drop" (the pivot), so the drop is either in `[lo, mid]` or
in `[mid, hi]`, never both. The half without the drop is ascending — which is
exactly what `nums[lo] <= nums[mid]` tests, since a sorted left half puts its
smallest element at `lo`.

*The range test is sound and complete for the sorted half.* If `nums[lo] <=
nums[mid]` then `nums[lo:mid + 1]` is ascending, so `nums[lo] <= target <
nums[mid]` is true iff `target` occurs in that half. Because values are
distinct and `nums[mid] != target` at this point, `target` is either in the
sorted half or in the other one; the `else` branch is therefore correct, not a
guess.

*Halving terminates correctly.* Both branches discard the midpoint and at least
half of the remaining elements, so the interval strictly shrinks; when it
becomes empty the target was never present (it was in the interval at every
step and each discard was justified).

## Complexity

- **Time:** O(log n) — one comparison-driven halving per iteration, at most
  `⌈log₂(n + 1)⌉` iterations; no scan of either half.
- **Space:** O(1) — `lo`, `hi`, and `mid` only, iterative (no recursion stack).

## Edge cases

- `nums == []` → `lo > hi` immediately → `-1`.
- Single element: found → `0`; not found → `-1`.
- No rotation at all (`nums` ascending) → falls back to textbook binary search.
- Rotation at the last position (`[1, 3, 5]` as `[5, 1, 3]`) → both branches
  exercised, target at either end found.
- Target at the pivot (the array's minimum), at index `0`, or at the last index.
- Target smaller than `nums[0]` or larger than every element → `-1` after the
  normal loop, no special casing.
- Negative values and values outside the array range → handled (comparisons
  only, no index arithmetic on values).
- Two-element arrays in both rotations (`[1, 3]`, `[3, 1]`).
- Duplicate values are **not** supported (the follow-up "Rotated Sorted Array
  II"): with `nums[lo] == nums[mid]` the sorted-half test is inconclusive and
  the search degrades to `O(n)`. This is the problem's stated precondition, not
  a bug — noted rather than silently mis-answering.
- Platform maximum (`5000`) is irrelevant to the runtime: 13 iterations.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[4,5,6,7,0,1,2]`, `0` | `4` | the statement's example |
| `[4,5,6,7,0,1,2]`, `3` | `-1` | absent, between the runs |
| `[1]`, `0` | `-1` | single element, absent |
| `[1]`, `1` | `0` | single element, present |
| `[]`, `5` | `-1` | empty array |
| `[1,3]`, `3` | `1` | unrotated pair, last index |
| `[3,1]`, `1` | `1` | rotated pair, last index |
| `[1,2,3,4,5,6]`, `4` | `3` | no rotation |
| `[5,1,3]`, `5` | `0` | target at index 0 after rotation |
| `[5,1,3]`, `3` | `2` | target at the last index |
| `[4,5,6,7,0,1,2]`, `7` | `3` | target just before the pivot |
| `[4,5,6,7,0,1,2]`, `1` | `5` | target just after the pivot |
| `[3,-2,-1,0,1]`, `-1` | `2` | negative values |
| `[3,-2,-1,0,1]`, `-3` | `-1` | below the minimum |
| every rotation of every sorted `0..n-1` for `n = 0..6`, targets `-2..n+1` | equals the linear scan | exhaustive differential check |
| 500 random sorted samples of `range(-200, 200)`, randomly rotated | equals the linear scan | randomized differential check |

## What I learned

- **Pattern:** binary search survives a broken ordering when a *local*
  invariant replaces the global one — here "one half is sorted", not "the whole
  array is sorted". Same shape as finding a peak: decide which side must contain
  the answer, then halve.
- **Pitfall:** writing the range tests with `<=` on both ends
  (`nums[lo] <= target <= nums[mid]`) looks harmless because `nums[mid] ==
  target` was already returned, but it silently re-admits the midpoint and, in
  the right-half branch, the wrong endpoint — the interval can then stop
  shrinking on a two-element input (`[3,1]` with target `1`).
- **Differently next time:** derive the branch from the sorted-half claim first
  ("which half is ascending, and where does that half's range end?") and only
  then write code; my first draft mixed the two branches' comparisons and the
  exhaustive rotation check over `n <= 6` caught it in seconds.

**Review date:** 2026-11-19 (1 day) · 2026-11-25 (7 days) · 2026-12-18 (30 days)
