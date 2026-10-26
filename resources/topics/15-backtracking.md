# 15 — Backtracking

> Phase 6 · Roadmap: see `ROADMAP.md` · File: `resources/topics/15-backtracking.md`

Recursion that explores a choice, and — crucially — **undoes** it before
trying the next one. The standard engine for "find *all* combinations."

## Purpose

Subsets, permutations, combinations, N-Queens, Sudoku: every
"enumerate the search space" problem is the same three-step loop. Backtracking
also teaches pruning, which is how exponential search spaces become
tractable.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Choose → explore → un-choose | the canonical loop body | write it without mutating shared state |
| Path / choices / goal | three explicit variables | restructure any such problem into them |
| Pruning | stop early when a partial path can't win | justify why the branch is dead |
| Duplicate avoidance | sort input / skip equal siblings | count combinations once, not n! times |
| Base case | path satisfies the goal → record a copy | record `path[:]`, never the live list |

## Key patterns

1. **Index-based subset** — for each index: take it, recurse, remove it.
2. **Combination with reuse** — same index allowed again for coin-style sums;
   advance index only when skipping.
3. **Permutation with used-flags** — `used[i]` marks consumed elements.
4. **Constraint propagation** — place a piece, recurse, undo (N-Queens,
   Sudoku).

## Complexity expectations

- Output size dominates: subsets `O(2^n)`, permutations `O(n!)`.
- Aim for the best *feasible* algorithm and prune; never claim polynomial
  time for exhaustive enumeration.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Subsets](https://leetcode.com/problems/subsets/) | Medium | include/exclude template |
| 2 | [Permutations](https://leetcode.com/problems/permutations/) | Medium | used-array template |
| 3 | [N-Queens](https://leetcode.com/problems/n-queens/) | Hard | constraint pruning |

## Prerequisites and follow-ups

- **Before this:** `14-recursion`.
- **Next:** `16-trees` — start Phase 7 (DFS on structures is backtracking).

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
