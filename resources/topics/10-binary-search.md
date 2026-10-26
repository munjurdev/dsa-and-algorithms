# 10 — Binary Search

> Phase 4 · Roadmap: see `ROADMAP.md` · File: `resources/topics/10-binary-search.md`

Searching a sorted array in `O(log n)` — and, more importantly, searching the
*answer space* of any monotone predicate in `O(log n · check)`.

## Purpose

Binary search is the one algorithm that scales problems with constraints of
`10⁹` down to microseconds. Learn the array form first, then the far more
powerful "binary search on answer" form (feasibility predicates).

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Invariant | answer lives in `[lo, hi)` and always shrinks | pick one convention and never deviate |
| `bisect_left/right` | Python's library implementation | know when each insertion point is right |
| Boundary search | first index with `predicate(x) == True` | lower/upper bound from scratch |
| Rotated arrays | search a shifted sorted range | decide which half is sorted |
| Binary search on answer | monotone "feasible(v)" over a value range | design the predicate, then binary search it |

## Key patterns

1. **Fixed template** — `lo, hi = 0, len(a)` / `while lo < hi` / return `lo`.
2. **"Minimize the maximum"** — guess capacity/days/threshold, test
   feasibility in `O(n)`.
3. **Peak/search-space reduction** — halve the range using an ordering hint.

## Complexity expectations

- `O(log n)` search × `O(f(n))` predicate → typically `O(n log n)` overall,
  which is what constraints of `10⁹` demand.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | textbook template |
| 2 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | find the sorted half |
| 3 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | binary search on answer |

## Prerequisites and follow-ups

- **Before this:** `09-sliding-window`, sorting basics.
- **Next:** `11-linked-list` — start Phase 5.

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
