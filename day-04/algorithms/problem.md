# Maximum Subarray

| Field | Value |
|---|---|
| Day | `day-04` |
| Track | `algorithms` |
| Topic | `02-arrays` — see `resources/topics/` |
| Difficulty | Medium |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/maximum-subarray/ |

## Problem summary

Given an integer array `nums`, return the largest possible sum of a
**non-empty** contiguous subarray. Values may be negative, so "take
everything" is not always best; the empty subarray is *not* allowed, which is
what makes the all-negative case a real trap. This is Kadane's algorithm: one
pass holding the best sum of a subarray **ending at the current index**, plus
the best seen so far.

### Input

- `nums: list[int]` — `1 <= len(nums) <= 10⁵`,
  `-10⁴ <= nums[i] <= 10⁴`, unsorted, negatives allowed.

### Output

- `int` — the maximum sum of any non-empty contiguous slice `nums[i:j+1]`.

## Approach

1. Initialise both registers with the first element:
   `best_ending_here = best = nums[0]`.
2. For every following value `x`, decide between extending the current run
   and restarting at `x`:
   `best_ending_here = max(x, best_ending_here + x)`.
3. Update the global answer: `best = max(best, best_ending_here)`.
4. Return `best` after the pass.

Step 2 is the whole insight: a run is worth keeping only while its partial sum
is positive, because a negative prefix can only drag down whatever follows.

## Why this approach works

For each index `j`, `best_ending_here` equals the maximum sum of a subarray
that **ends exactly at `j`**. Any such subarray is either `[nums[j]]` alone or
a maximum-sum subarray ending at `j - 1` extended by `nums[j]`; since the
extension adds the same `nums[j]` in both cases, the maximum over all of them
is `max(nums[j], best_ending_here(j-1) + nums[j])`. By induction this is exact
at every `j`, and the overall answer is the maximum over all end points — so
the single register pair captures every candidate subarray without ever
enumerating one. Initialising from `nums[0]` (rather than `0`) is what keeps
the all-negative answer a single element instead of the forbidden empty sum.

## Complexity

- **Time:** O(n) — one pass, constant work per element.
- **Space:** O(1) — two integers, regardless of input size.

## Edge cases

- All negatives, e.g. `[-3, -1, -2]` → `-1`: restarting at each element is
  never better than keeping a negative run, so the maximum single element
  wins. Initialising `best = 0` would wrongly return `0`.
- Single element: `[-1]` → `-1`, `[0]` → `0`.
- Single positive element: `[5]` → `5`.
- Zeros interleaved with negatives: `[0, -1]` → `0`; a zero run is a valid
  subarray, so it beats the negative tail.
- Empty input → `ValueError`, since no non-empty subarray exists.
- Mixed large positives around a big negative: `[5, 4, -1, 7, 8]` → `23` —
  the negative is worth absorbing, not skipping.
- Maximum constraints (`10⁵` elements near `±10⁴`): sums stay under `10⁹`,
  well inside any fixed-width integer; Python ints are unbounded anyway.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` | `6` | statement example: `[4, -1, 2, 1]` |
| `[1]` | `1` | single element |
| `[5, 4, -1, 7, 8]` | `23` | absorbing one negative beats splitting |
| `[-3, -1, -2]` | `-1` | all negative: best single element, not `0` |
| `[-1]` | `-1` | all-negative single element |
| `[0, -1]` | `0` | the zero element alone beats the negative tail |
| `[-2, -1]` | `-1` | never let the run fall below the element itself |
| `[]` | raises `ValueError` | no non-empty subarray exists |
| 300 random arrays (size 1–30, values `-10…10`) | equals `O(n²)` brute force | differential check on every slice |

## What I learned

- **Pattern:** running state that answers "best ending **here**" — the same
  shape as Two Sum's map, one register instead of a table. Subarray DP is
  Kadane once you notice step 2 only needs the previous index.
- **Pitfall:** initialising `best = 0` looks harmless and silently breaks
  every all-negative input; the correct seed is the first element.
- **Differently next time:** decide *before* coding whether the empty
  subarray is legal — that single question fixes both the initialisation and
  the return value for the whole edge-case family.

**Review date:** 2026-11-06 (1 day) · 2026-11-12 (7 days) · 2026-12-05 (30 days)
