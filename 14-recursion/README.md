# 14 — Recursion

> Phase 6 · Roadmap Days 097–103 · Folder: `14-recursion/`

A function that calls a smaller version of itself — the mental model behind
trees, backtracking, and most dynamic programming.

## Purpose

Recursion lets you *state the solution at the level of the whole problem*
("the answer for n is built from the answers for n-1") instead of tracking
every variable yourself. Learn it properly here, because Phase 6–9 are all
recursion with different shapes.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Base case | smallest input with a direct answer | write it before anything else |
| Recursive case | express the answer using smaller calls | trust it — don't unroll mentally |
| Call stack | each call is a frame; depth = `O(n)` worst case | spot stack-overflow risk |
| Recurrence | define `T(n)` in terms of `T(n/k)` | analyze with the master theorem |
| Tail vs non-tail | last action is the recursive call | convert tail calls to iteration when needed |

## Key patterns

1. **Range recursion** — `f(lo, hi)` splits at a midpoint (merge sort, quick
   sort, binary search on trees).
2. **Index recursion** — `f(i)` over an array/string (subsets, palindromes).
3. **Structure recursion** — recurse on `node.left` / `node.right` (preview of
   `16-trees`).
4. **Helper with accumulator** — carry state in an argument instead of a
   global.

## Complexity expectations

- Count *calls × work per call*. `f(n) = 2·f(n-1)` is `O(2^n)`; without
  memoization, overlapping subproblems get recomputed exponentially — that
  pain motivates `21-dynamic-programming`.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | first recurrence, `O(2^n)` → `O(n)` |
| 2 | Reverse a linked list recursively | Easy | base case + smaller call |
| 3 | Generate all subsets | Medium | include/exclude recursion (bridge to backtracking) |

## Prerequisites and follow-ups

- **Before this:** `12-stack` (the call stack), Python fundamentals.
- **Next:** `15-backtracking` — recursion with undo and pruning.

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
