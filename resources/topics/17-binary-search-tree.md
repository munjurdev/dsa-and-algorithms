# 17 — Binary Search Tree

> Phase 7 · Roadmap: see `ROADMAP.md` · File: `resources/topics/17-binary-search-tree.md`

A binary tree with an ordering invariant: left < node < right. Structure and
order in one shape gives `O(log n)` search — *if* the tree stays balanced.

## Purpose

BSTs combine the traversal skills from `16-trees` with a global invariant,
which is exactly what interviewers probe: "what can you guarantee, and when
does it degrade?" Ordered traversal of a BST also produces sorted output —
a common trick.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| The invariant | every node's left subtree < node < right subtree | validate a tree against it |
| Search / insert / delete | walk down using comparisons | handle the 3 deletion cases |
| In-order traversal | visits keys in sorted order | find k-th smallest in `O(h + k)` |
| Degenerate trees | sorted inserts → linked list `O(n)` | explain why balance matters |
| Height | `O(log n)` if balanced, `O(n)` if not | relate height to operation cost |

## Key patterns

1. **Bounded recursion** — carry `(low, high)` valid ranges; invalid → stop
   (validation, closest value, two-sum-in-BST).
2. **In-order streaming** — iterator / k-th smallest without building a list.
3. **Split & merge** — delete by merging subtrees; balance via in-order
   rebuild.

## Complexity expectations

- Search/insert/delete: `O(h)` where `h` is the height — `O(log n)` balanced,
  `O(n)` degenerate. Be explicit about which you assume.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | bounds, not just local compare |
| 2 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | in-order traversal |
| 3 | Insert into a Binary Search Tree | Medium | walk and attach |

## Prerequisites and follow-ups

- **Before this:** `16-trees`.
- **Next:** `18-heaps-and-priority-queue`, then Phase 8 graphs.

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
