# Container With Most Water

| Field | Value |
|---|---|
| Day | `day-08` |
| Track | `algorithms` |
| Topic | `07-two-pointers` — see `resources/topics/` |
| Difficulty | Medium |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/container-with-most-water/ |

## Problem summary

Each element `heights[i]` is the height of a vertical line standing at
position `i`. Pick two lines; together with the x-axis they form a container
that holds `(j - i) * min(heights[i], heights[j])` units of water. Return the
largest area available. The straightforward answer tries every pair; the
interesting part is proving that a single converging pass is enough.

### Input

- `heights: list[int]` — non-negative heights, `2 <= len(heights) <= 10⁵` on
  the platform, values `0 <= heights[i] <= 10⁴`.
- This implementation is total: fewer than two lines return `0`.

### Output

- `int` — the maximum area; `0` when no two lines exist or every candidate
  pair includes a zero-height line.

## Approach

1. Set `left = 0`, `right = n - 1` — the widest possible container — and
   `best = 0`.
2. Compute `width = right - left` and
   `area = width * min(heights[left], heights[right])`, updating `best`.
3. **Move the shorter line inward** (ties move `left`). Never move the taller
   one. Repeat until `left >= right`.
4. Return `best`.

No nested loop, no sorting, no extra structure — the algorithm is the greedy
movement rule plus a single measured value per step.

## Why this approach works

**The pointer being moved is provably safe to retire.** Suppose
`heights[left] <= heights[right]`. For every partner `k` with
`left < k <= right`, the area is
`(k - left) * min(heights[left], heights[k])`, and `min(...) <= heights[left]`
because the shorter line caps the container. Also `k - left <= right - left`.
So no container using `left` with any remaining partner can beat the one just
measured at the current width. Whatever the optimum is, it does not need
`left`, and moving `left` inward cannot skip it.

**The argument is symmetric.** When `heights[right] < heights[left]`, the same
reasoning retires `right`: any narrower container using it is capped by
`heights[right]` and has less width.

**Completeness.** Each step removes exactly one line from consideration and
proves no optimal pair used it. The best area is recorded before that
retirement, so the maximum over all remaining candidate pairs is preserved.
When the pointers meet, every pair that could be optimal has been evaluated —
directly or displaced by a container at least as good. This is the classic
"move the smaller side" argument, and it is why the greedy pass is exact
rather than heuristic.

**Why not sort?** Sorting destroys the positions, and width depends on index
distance. Two pointers here converge in place instead.

## Complexity

- **Time:** O(n) — each iteration moves one pointer inward, so at most
  `n - 1` iterations, each doing constant work.
- **Space:** O(1) — two indices and one running maximum; the input is never
  copied or mutated.

## Edge cases

- Empty list or a single line → `0`; no container exists.
- Two lines → only one pair, so the area is `min(h[0], h[1])`.
- Equal heights `[5, 5, 5, 5]` → `15` from the widest pair.
- A zero line anywhere pair: `[0, 5, 0]` → `0`, since every pair includes a
  zero.
- Strictly increasing `[1, 2, 3, 4, 5]` → `6`, and strictly decreasing
  `[5, 4, 3, 2, 1]` → `6`; neither is the widest pair.
- Tall lines far apart still lose height to a short partner, so the best pair
  is not necessarily the two tallest.
- Platform-valid sizes are always ≥ 2; the `0` return is extra safety, not a
  reinterpretation of the statement.
- Input is not mutated, so callers can reuse `heights`.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[1, 8, 6, 2, 5, 4, 8, 3, 7]` | `49` | the statement's example |
| `[1, 1]` | `1` | exactly one pair |
| `[4, 3]`, `[3, 4]` | `3` | shorter line caps it |
| `[]`, `[7]` | `0` | no pair exists |
| `[0, 0]`, `[0, 5, 0]` | `0` | every pair includes a zero line |
| `[5, 5, 5, 5]` | `15` | widest pair with equal heights |
| `[1, 2, 3, 4, 5]` | `6` | increasing profile |
| `[5, 4, 3, 2, 1]` | `6` | decreasing profile |
| `[1000, 1, 1, 1, 1000]` | `4000` | equal tall lines, width decides |
| `[2, 3, 10, 5, 7, 8, 9]` | `36` | the two tallest are not the answer |
| every array of length 0–7 over `0…5` | equals an every-pair oracle | exhaustive differential check |
| 400 random arrays of length 0–60 | equals the every-pair oracle | randomized differential check |

## What I learned

- **Pattern:** when the objective is `width * min(heights)`, the *limiting*
  side is the only thing worth changing — move the bottleneck, not the side
  that is already tall enough.
- **Pitfall:** "move the shorter side" is easy to state and easy to
  mis-remember as "move the left pointer when left is shorter". Getting the
  tie case wrong is still correct here (moving either is safe), but moving the
  *taller* side silently skips the optimum — the brute-force oracle catches it
  instantly.
- **Differently next time:** write the safety proof before the loop. One
  sentence — every narrower container using the shorter line is capped by that
  same height — is the whole algorithm, and it makes the code almost
  mechanical.

**Review date:** 2026-11-11 (1 day) · 2026-11-17 (7 days) · 2026-12-10 (30 days)
