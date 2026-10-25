# 13 — Queue and Deque

> Phase 5 · Roadmap Days 091–096 · Folder: `13-queue-and-deque/`

First in, first out — plus the double-ended queue that makes sliding-window
extrema and BFS possible in `O(n)`.

## Purpose

Queues model *processing order* (tasks, levels, messages) and are the engine
underneath BFS. Deques add the second port, enabling monotonic-deque
optimizations and `O(1)` operations at both ends that lists cannot do efficiently.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| FIFO queue | enqueue at back, dequeue at front | use `collections.deque`, never `list.pop(0)` |
| Circular buffer | fixed-size ring, wrap-around index | design a circular queue yourself |
| Deque | `O(1)` push/pop at both ends | sliding window maximum in `O(n)` |
| Monotonic deque | candidates ordered, pop stale ones from front | max/min over all windows |
| Blocked queue / priority | ordering variants (see heaps for PQ) | know when a queue is not enough |

## Key patterns

1. **Two-stack simulation** → queue; **two-queue simulation** → stack
   (great exercises for internals).
2. **Monotonic decreasing deque** — evict indices that fell out of the window
   from the front, evict smaller values from the back.
3. **Level-by-level BFS** — `for _ in range(len(q))` marks one level (preview
   of `19-graphs`).

## Complexity expectations

- Amortized `O(1)` per queue/deque operation.
- Monotonic deque scans: `O(n)` total (each index enters and leaves once).

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Easy | amortized `O(1)` peek |
| 2 | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | Medium | ring buffer indices |
| 3 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | monotonic deque |

## Prerequisites and follow-ups

- **Before this:** `12-stack`, `09-sliding-window`.
- **Next:** `14-recursion` — start Phase 6.

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
