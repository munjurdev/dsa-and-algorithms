# Spiral Matrix

| Field | Value |
|---|---|
| Day | `day-05` |
| Track | `algorithms` |
| Topic | `04-matrices` — see `resources/topics/` |
| Difficulty | Medium |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/spiral-matrix/ |

## Problem summary

Given an `m × n` matrix, return every element in clockwise spiral order:
the top row left to right, the right column downwards, the bottom row right to
left, the left column upwards, then the same walk on the next inner ring until
the whole grid is consumed. This is layer peeling with four shrinking
boundaries — no visited grid, so the extra space is `O(1)`.

### Input

- `matrix: list[list[int]]` — `1 <= m, n <= 10`, `-100 <= matrix[r][c] <= 100`.
- Rows must be rectangular: every row has the same length, at least one column.

### Output

- `list[int]` — the `m · n` values in spiral order, each exactly once.

## Approach

1. Set four boundaries around the still-unvisited rectangle: `top = 0`,
   `bottom = m - 1`, `left = 0`, `right = n - 1`.
2. While `top <= bottom` and `left <= right`:
   1. Walk the top edge, columns `left … right` on row `top`; then `top += 1`.
   2. Walk the right edge, rows `top … bottom` on column `right`; then
      `right -= 1`.
   3. **Only if `top <= bottom`**, walk the bottom edge, columns
      `right … left` on row `bottom`; then `bottom -= 1`.
   4. **Only if `left <= right`**, walk the left edge, rows
      `bottom … top` on column `left`; then `left += 1`.
3. Return the collected values.

## Why this approach works

One loop iteration consumes exactly the border of the current rectangle in
clockwise order, then shrinks that rectangle by one on each side, so the cell
set visited so far is always the prefix of the spiral and the remaining cells
always form another (possibly empty) rectangle. Each cell belongs to exactly
one border at the moment it is reached, so every value is emitted exactly
once. The two guard checks exist for the degenerate rectangles: after the top
row is taken, a single-row board has `top > bottom`, and after the right
column is taken, a single-column board has `left > right`. Without the guards
the bottom and left edges would re-emit the row or column just consumed.

## Complexity

- **Time:** O(m · n) — every cell is appended exactly once, with constant work
  per cell.
- **Space:** O(1) auxiliary — four indices; the returned list is the `m · n`
  output and is not counted (a visited-grid solution would need `O(m · n)`
  extra).

## Edge cases

- Empty matrix `[]` → `[]`: there is nothing to peel.
- No columns, e.g. `[[]]` → `ValueError`: a grid with zero columns is not a
  valid matrix, and silently returning `[]` would hide the malformed input.
- Ragged matrix (rows of different length) → `ValueError`, raised before any
  walking, so no index ever goes out of range.
- Single element `[[7]]` → `[7]`: the top edge emits it, then both boundaries
  cross and the loop ends.
- `1 × n` (one row): after the top edge, `top > bottom`, so the bottom edge is
  skipped — the classic bug is emitting the row a second time in reverse.
- `n × 1` (one column): the top edge emits the first cell, the right edge
  walks the rest downwards, and the left edge is skipped because
  `left > right` — again, the guard is what prevents duplication.
- Square boards: `2 × 2`, `3 × 3`, `4 × 4` end exactly on a full ring, so the
  loop exits on crossed boundaries rather than mid-edge.
- Boards with a leftover inner row or column: `3 × 2` and `2 × 3` hit step 3 or
  step 4 with a degenerate remainder; both are handled by the guards.
- Maximum size (`10 × 10`): 100 cells, still `O(m · n)`, no recursion.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` | `[1, 2, 3, 6, 9, 8, 7, 4, 5]` | statement's square example |
| `[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]` | `[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]` | `3 × 4`: right edge, then inner ring |
| `[[1, 2, 3]]` | `[1, 2, 3]` | `1 × n`: bottom edge must be skipped |
| `[[1], [2], [3]]` | `[1, 2, 3]` | `n × 1`: left edge must be skipped |
| `[[7]]` | `[7]` | single cell |
| `[[1, 2], [3, 4]]` | `[1, 2, 4, 3]` | `2 × 2` ends on a complete ring |
| `[[1], [2]]` | `[1, 2]` | two rows, one column |
| `[[1, 2]]` | `[1, 2]` | one row, two columns |
| `[[1, 2, 3], [4, 5, 6]]` | `[1, 2, 3, 6, 5, 4]` | `2 × 3` with a leftover bottom edge |
| `[[1, 2], [3, 4], [5, 6]]` | `[1, 2, 4, 6, 5, 3]` | `3 × 2` with a leftover left edge |
| `[]` | `[]` | no cells to peel |
| `[[]]` | raises `ValueError` | grid with no columns |
| `[[1, 2], [3]]` | raises `ValueError` | ragged rows |
| 400 random `m × n` matrices, `1 <= m, n <= 6` | equal to a direction-walk reference | differential check on every shape |
| a `10 × 10` matrix of `0…99` | sorted output equals `0…99` | every cell emitted exactly once |

## What I learned

- **Pattern:** a spiral is a shrinking rectangle — four boundary indices, not
  a direction array and not a visited grid. The same four-index shape rotates
  an image and peels a matrix in place.
- **Pitfall:** `while top <= bottom and left <= right` is not enough on its
  own; the bottom and left edges need their *own* guards, or `1 × n` and
  `n × 1` boards emit their shared row/column twice.
- **Differently next time:** write the guards as the question they answer —
  "does a row still remain after the top edge?" — instead of copying
  `if top <= bottom` from a template; the reason is what makes the bugs stop.

**Review date:** 2026-11-08 (1 day) · 2026-11-14 (7 days) · 2026-12-07 (30 days)
