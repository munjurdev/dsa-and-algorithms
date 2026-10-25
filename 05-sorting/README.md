# 05 — Sorting

> Phase 2 · Roadmap Days 035–040 · Folder: `05-sorting/`

Sorting is both a tool you use constantly and an algorithm family you must be
able to derive: comparison sorts, `O(n)` counting sorts, and custom comparators.

## Purpose

Half of all interview solutions start with "sort it, then scan." This topic
builds that reflex and teaches you *when sorting is the bottleneck* and when
a linear alternative (hashing, bucket/radix tricks) beats it.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Comparison sorts | Any comparison-based sort is `Ω(n log n)` | prove the bound (decision tree) |
| Merge sort | Split, sort, merge — stable, `O(n log n)` | implement the merge step from memory |
| Quick sort | Partition around a pivot | state average vs worst case |
| Insertion sort | Grow a sorted prefix | use for tiny or nearly-sorted arrays |
| Counting / bucket sort | `O(n)` when the key range is small | count occurrences to find the k-th element |
| Python's `sorted` | Timsort — stable, `O(n log n)` | key functions, multi-key sort, `reverse` |

## Key patterns

1. **Sort by a custom key** — `key=lambda p: (p[0], -p[1])` for tuples.
2. **Sort then two pointers / binary search** — the universal combo.
3. **Sort by interval end** — greedy interval scheduling (see `25-intervals`).
4. **Nth element via heap or quickselect** — `O(n)` average selection.

## Complexity expectations

- Default: `O(n log n)` time, `O(n)` space for Python's sort (stable).
- Recognize when a key range `≤ n` allows `O(n)` counting.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | Dutch national flag, in place |
| 2 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | sort by start, linear merge |
| 3 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | heap vs quickselect |

## Prerequisites and follow-ups

- **Before this:** `02-arrays`, `01-complexity-analysis`.
- **Next:** `06-hashing` — start Phase 3.

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
