# 04 — Matrices

> Phase 2 · Roadmap Days 031–034 · Folder: `04-matrices/`

Two-dimensional arrays: grid traversal, in-place transformation, and matrix
indexing — the shape of problems from image rotation to island counting.

## Purpose

Matrices exercise the exact skills interviews reward most: coordinate
reasoning, visited tracking, and clean nested iteration. The same traversal
ideas reappear in graphs (grid as an implicit graph) and DP (2-D tables).

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Index pairs `(r, c)` | A cell is a coordinate, not a value | convert between index and position |
| Direction arrays | `[(1,0),(-1,0),(0,1),(0,-1)]` | walk 4-neighbours without repetition |
| Layer traversal | Spiral = peel the outer ring | implement spiral order in `O(1)` extra space |
| Transpose & reverse | Rotate = transpose then mirror | rotate 90° in place |
| In-place marking | Write a sentinel, then restore | zero a matrix without extra rows |

## Key patterns

1. **Visited grid** — `set()` of coordinates or mutate the cell (mark/restore).
2. **BFS/DFS on a grid** — flood fill an entire component from one seed.
3. **Layer by layer** — spiral, rotation, and border problems are all "peel
   the ring."

## Complexity expectations

- Every cell is visited `O(1)` times → `O(m·n)` time and `O(m·n)` space for
  visited markers (or `O(1)` extra if you mutate in place).

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | layer traversal |
| 2 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | in-place transpose/mirror |
| 3 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | in-place marking, `O(1)` space |

## Prerequisites and follow-ups

- **Before this:** `02-arrays`, `03-strings`.
- **Next:** `05-sorting`, then hashing; grids return in `19-graphs`.

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
