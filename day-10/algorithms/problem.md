# Maximum Average Subarray I

| Field | Value |
|---|---|
| Day | `day-10` |
| Track | `algorithms` |
| Topic | `09-sliding-window` (fixed-size window) — see `resources/topics/` |
| Difficulty | Easy |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/maximum-average-subarray-i/ |

## Problem summary

Given an integer array `nums` and an integer `k`, find the contiguous subarray
of length exactly `k` with the largest average, and return that average. Because
every candidate has the same denominator `k`, maximizing the average is the same
as maximizing the window **sum** — which turns the problem into one pass with a
running fixed-size window.

### Input

- `nums: list[int]` — `1 <= len(nums) <= 10⁵` on the platform, values
  `-10⁴ <= nums[i] <= 10⁴`; negatives and zeros are allowed.
- `k: int` — `1 <= k <= len(nums)` on the platform.
- This implementation is total: `k <= 0` and `k > len(nums)` raise
  `ValueError`, because no window of that length exists.

### Output

- `float` — `max(sum(nums[i:i + k]) / k)` over `0 <= i <= len(nums) - k`.
  Platform answers are accepted within `10⁻⁵`.

## Approach

1. Validate: reject `k <= 0` and `k > len(nums)` with `ValueError`.
2. Compute the first window's sum, `sum(nums[:k])`, and make it the best.
3. Slide `right` from `k` to `n - 1`:
   `window_sum += nums[right] - nums[right - k]`, then keep the maximum.
4. Return `best_sum / k` — one exact division at the very end.

Each slide replaces one leaving element with one entering element, so no window
is ever re-summed.

## Why this approach works

**Invariant (one sentence):** at the top of each slide step,
`window_sum == sum(nums[right - k : right])`, the sum of the last `k` elements
seen so far.

*It is maintained exactly.* Before the step the invariant says
`window_sum = nums[right-k] + … + nums[right-1]`; the update adds `nums[right]`
and subtracts `nums[right-k]`, leaving `nums[right-k+1] + … + nums[right]`,
which is the invariant with `right` incremented by one. Adding and subtracting
integers is exact, so no rounding creeps in.

*Maximum sum ⇒ maximum average.* All windows share the positive denominator
`k`, and division by a positive constant is strictly increasing, so the window
with the largest sum has the largest average. That is why the code never tracks
an average inside the loop — and why dividing only once at the end avoids
comparing `n - k + 1` rounded floats.

*The loop covers every window.* The first window is handled before the loop,
and each iteration introduces exactly one new right end, so all
`n - k + 1` windows are visited exactly once.

## Complexity

- **Time:** O(n) — one pass: the initial window costs `O(k)` and each of the
  `n - k` slides costs `O(1)` arithmetic.
- **Space:** O(1) — two integer sums plus loop indices; no prefix array, no
  copy of the input.

## Edge cases

- `k = 1` → the maximum element (as a float), e.g. `[1, 2, 3, 4], 1` → `4.0`.
- `k = len(nums)` → the average of the whole array: `[1, 2, 3, 4], 4` → `2.5`.
- Single element: `[5], 1` → `5.0`; `[-1], 1` → `-1.0`.
- All negatives: `[-5, -3, -8, -1], 2` → `-4.0` — the best window is
  `[-5, -3]`; initializing the best to `0` would be wrong here.
- Zeros: `[0, 0, 0, 0, 0], 3` → `0.0`.
- Best window at the boundary: `[10, 0, 0, 0, 1], 2` → `5.0` (first window);
  `[0, 0, 0, 1, 10], 2` → `5.5` (last window).
- Fractional results: `[1, 2], 2` → `1.5`; `[2, -1, 2, -1, 2], 3` → `1.0`.
- Return type is always `float`, even for integral averages.
- Invalid windows: `k = 0`, `k = -1`, and `k > len(nums)` raise `ValueError`
  instead of returning a meaningless number.
- Input is never mutated; the caller can reuse `nums`.
- Maximum constraints (`10⁵` elements, `±10⁴` values) keep sums within `±10⁹`,
  which is exact in Python ints and safe in 64-bit too.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[1, 12, -5, -6, 50, 3], 4` | `12.75` | the statement's example |
| `[5], 1` | `5.0` | single element |
| `[-1], 1` | `-1.0` | negative single element |
| `[1, 2, 3, 4], 4` | `2.5` | `k = n` |
| `[1, 2, 3, 4], 1` | `4.0` | `k = 1`, maximum element |
| `[-5, -3, -8, -1], 2` | `-4.0` | all negatives: best is least negative |
| `[-10000], 1` | `-10000.0` | platform minimum value |
| `[0, 0, 0, 0, 0], 3` | `0.0` | zero average |
| `[0, 4, 0, 3, 2], 1` | `4.0` | zeros around the maximum |
| `[10, 0, 0, 0, 1], 2` | `5.0` | best window is the first |
| `[0, 0, 0, 1, 10], 2` | `5.5` | best window is the last |
| `[1, 2], 2` | `1.5` | fractional average |
| `[2, -1, 2, -1, 2], 3` | `1.0` | many equal sums |
| `[1, 2, 3], k ∈ {0, -1, 5}` | `ValueError` | no such window exists |
| every array of length 1–6 over `-3…3`, every `1 <= k <= n` | equals an `O(n·k)` brute force | exhaustive differential check |
| 500 random arrays of length 1–40 over `-10…10` | equals the brute force | randomized differential check |

## What I learned

- **Pattern:** a fixed-size window can be updated by `+ entering - leaving`,
  so `n - k` slides cost `O(1)` each; the running sum *is* the state.
- **Pitfall:** seeding `best` with `0` looks harmless and passes the
  all-positive example, but silently breaks every all-negative array. Seeding
  with the first window's sum is the only choice that is correct by
  construction.
- **Differently next time:** notice up front that the denominator is shared,
  compare sums as integers, and divide once — it removes float comparison and
  makes the invariant trivially exact.

**Review date:** 2026-11-12 (1 day) · 2026-11-18 (7 days) · 2026-12-11 (30 days)
