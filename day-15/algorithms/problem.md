# Sliding Window Maximum

| Field | Value |
|---|---|
| Day | `day-15` |
| Track | `algorithms` |
| Topic | `13-queue-and-deque` — see `resources/topics/` (also `09-sliding-window`) |
| Difficulty | Hard |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/sliding-window-maximum/ |

## Problem summary

Given an integer array and a window width `k`, return the maximum of every
contiguous subarray of length `k`. The windows overlap by `k - 1` elements, so
recomputing each maximum throws away almost all of the previous work: the
interesting cases are monotone runs, where one element stays the maximum for
many windows, and the transition where the old maximum slides out and the next
one must already be known. A decreasing deque of candidate indices answers
both in O(1) per step.

### Input

- `nums: list[int]` — length `1..10⁵`, values in `-10⁴..10⁴` (duplicates and
  negatives allowed).
- `k: int` — `1 <= k <= len(nums)`.

### Output

- `list[int]` — length `len(nums) - k + 1`; element `i` is
  `max(nums[i : i + k])`.

## Approach

1. Keep `candidates`, a deque of **indices** whose values are strictly
   decreasing from front to back, and `result`.
2. For each `index, value`:
   - while the back of the deque has a value `<= value`, pop it — that element
     can never be the maximum of this or any later window that contains `value`;
   - append `index`;
   - let `window_start = index - k + 1`; if `candidates[0] < window_start`,
     popleft it (the front has slid out);
   - if `window_start >= 0`, append `nums[candidates[0]]`.
3. Return `result`.

## Why this approach works

**Invariant (one sentence):** just before reading the answer, the deque holds,
in increasing index order, exactly the indices of the current window whose
values are strictly decreasing — so its front is the window's maximum and every
other index in it is a future candidate that has not yet been outlived.

*Discarding from the back is safe.* If `nums[back] <= value` and the back index
is inside the window containing `value`, then every window that used the back
index also contains `value` (it is newer) and `value` is at least as large, so
the back can never be the answer again. Equal values are popped too, which is
why the deque stays strictly decreasing and the front is unambiguous.

*Discarding from the front is exact.* The front index is the oldest surviving
candidate; once it is less than `window_start` it is outside the window and can
never re-enter, because windows only move right. No other index in the deque can
be expired, since indices increase front-to-back.

*The total work is linear.* Each index is appended exactly once and removed at
most once (from the back by the value rule or from the front by the expiry
rule), so the inner loops run at most `2n` times across the whole scan — the
O(n) bound is counting amortized removals, not a per-element cost.

## Complexity

- **Time:** O(n) — one pass, each index appended once and popped at most once;
  every other operation is O(1). Compare with O(n·k) for re-scanning windows
  and O(n log k) for a heap with lazy deletion.
- **Space:** O(k) — the deque never holds more than the `k` indices of one
  window (plus the result, which is O(n) by definition).

## Edge cases

- `k = 1` → each element is its own window; output equals input, including
  negatives and duplicates.
- `k = len(nums)` → exactly one window; its maximum, whatever the order.
- `nums` empty → `[]`; `k > len(nums)` → `[]` (defensive — the platform
  excludes both), `k <= 0` → `ValueError`.
- All elements equal → each new value pops the previous back, so the deque
  always has length 1 and every window reports the same value.
- Strictly increasing input → the back is popped on every step; result is
  `nums[k-1:]`.
- Strictly decreasing input → nothing is ever popped from the back; the front
  expires exactly once per step; result is `nums[:len(nums)-k+1]`.
- Negatives → no sentinel such as `0` is used; a zero-initialized "current max"
  would be wrong here.
- Duplicates at the window boundary → the `<=` pop and the `< window_start`
  expiry must both be non-strict *in the right place*: `<=` on the back keeps
  only the newest equal maximum, `<` on the front keeps an element exactly `k`
  positions away.
- Maximum size (10⁵) → the full-size increasing and decreasing shapes are
  asserted in `main()`, since they stress opposite ends of the deque.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[1,3,-1,-3,5,3,6,7]`, 3 | `[3,3,5,5,6,7]` | the statement's example |
| `[1]`, 1 | `[1]` | single window of width 1 |
| `[1,-1]`, 1 | `[1,-1]` | negatives are not filtered by a zero sentinel |
| `[9,11]`, 2 | `[11]` | minimum window wider than 1 |
| `[4,-2]`, 2 | `[4]` | maximum is the first element |
| `[-7,-8,7,5,7,1,6,0]`, 4 | `[7,7,7,7,7]` | negatives, duplicates, one dominant value |
| `[]`, 1 | `[]` | empty array |
| `[1,2]`, 3 | `[]` | window wider than the array |
| `[1,2,3,4,5]`, 5 | `[5]` | `k = n`, increasing |
| `[5,4,3,2,1]`, 5 | `[5]` | `k = n`, decreasing |
| `[2,2,2,2]`, 2 | `[2,2,2]` | all equal |
| 500 random arrays (size 0–60, values −50..50), random `k` | brute-force maxima | randomized differential check |
| `range(1,100001)`, 1000 | `range(1000,100001)` | full-size increasing, back pops on every step |
| `range(100000,0,-1)`, 1000 | `100000, 99999, …` | full-size decreasing, front expiry on every step |

## What I learned

- **Pattern:** a monotonic deque is "the window's candidates in sorted order,
  with the stale ones at the front". The same shape gives sliding-window
  minimum by flipping the comparison, and the monotonic *stack* from Day 14 is
  the same discard argument without the expiry rule.
- **Pitfall:** the two ends have different removal reasons and must be handled
  in the right order. Popping smaller values from the back is a dominance
  argument; popping the expired front is a window argument. Reading the front
  before checking expiry reports a maximum that has already left the window —
  and the statement example can hide it, because its front often expires while
  a larger value is behind it.
- **Differently next time:** include the monotone increasing and decreasing
  inputs at full size from the start. They are the two inputs that exercise
  each end of the deque, so they expose an order bug that random tests may take
  many cases to hit.

**Review date:** 2026-11-22 (1 day) · 2026-11-28 (7 days) · 2026-12-21 (30 days)
