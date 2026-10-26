# 16 — Trees

> Phase 7 · Roadmap: see `ROADMAP.md` · File: `resources/topics/16-trees.md`

Hierarchical data with exactly one parent per node: the structure where BFS,
DFS, recursion, and divide-and-conquer all meet in one problem family.

## Purpose

Binary trees appear in interviews more than any other non-linear structure.
Mastery means fluency with the two traversals, the "solve for one node in
terms of the children" recursive style, and level-order BFS with a queue.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Node / root / leaf / height | the vocabulary | compute height and depth safely |
| Pre/in/post-order | DFS visit orders | implement all three iteratively too |
| Level order (BFS) | frontier queue, level by level | group results per level |
| Recursion on subtrees | `f(node) = combine(f(left), f(right))` | derive depth/diameter/path-sum |
| Construct from traversals | rebuild with bounds or index maps | preorder+inorder → tree |

## Key patterns

1. **Post-order combine** — process children first, then the node (height,
   diameter, path sums).
2. **BFS with a level loop** — `for _ in range(len(q))` per level.
3. **Top-down pass** — carry inherited context (path prefix, coordinate).
4. **Serialize/deserialize** — flatten with markers, rebuild from the stream.

## Complexity expectations

- Every traversal: `O(n)` time (each node once), `O(n)` space worst case for
  the recursion stack/queue; balanced tree recursion depth is `O(log n)`.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | BFS by level |
| 2 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | post-order recursion |
| 3 | Construct Binary Tree from Preorder and Inorder | Medium | divide and conquer with index maps |

## Prerequisites and follow-ups

- **Before this:** `14-recursion`, `15-backtracking`, `13-queue-and-deque`.
- **Next:** `17-binary-search-tree`, `18-heaps-and-priority-queue`.

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
