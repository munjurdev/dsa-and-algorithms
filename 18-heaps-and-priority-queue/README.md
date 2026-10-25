# 18 — Heaps and Priority Queues

> Phase 7 · Roadmap Days 127–131 · Folder: `18-heaps-and-priority-queue/`

A tree that keeps the minimum (or maximum) at the root, maintained in
`O(log n)` per operation — "give me the next best thing, quickly."

## Purpose

Whenever a problem says *k-th largest*, *top k frequent*, *merge k streams*,
or *nearest/cheapest among candidates*, a heap is the natural tool. It is the
standard alternative when binary search and two pointers don't fit.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Binary heap as an array | children at `2i+1`, `2i+2` | index arithmetic without a picture |
| Sift-up / sift-down | restore the heap property after a change | trace both operations by hand |
| Heapify | build a heap in `O(n)` | know why it beats n inserts |
| Python's `heapq` | min-heap on a plain list | max-heap via negated keys |
| Size-bounded heap | keep only k elements | top-k with `O(n log k)` |

## Key patterns

1. **Fixed-size max/min heap of size k** — running top-k in one pass.
2. **Two heaps** — max-heap of the lower half, min-heap of the upper half →
   running median.
3. **Merge k sorted streams** — push heads, pop smallest, push its successor.
4. **Lazy removal** — pop stale entries instead of deleting (Dijkstra).

## Complexity expectations

- Push/pop `O(log n)`, peek `O(1)`, heapify `O(n)`.
- Top-k by a single scan: `O(n log k)` time, `O(k)` space.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | size-k heap |
| 2 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Counter + heap |
| 3 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | two-heap technique |

## Prerequisites and follow-ups

- **Before this:** `16-trees`, `17-binary-search-tree`, `05-sorting`.
- **Next:** `19-graphs` — heaps make Dijkstra possible.

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
