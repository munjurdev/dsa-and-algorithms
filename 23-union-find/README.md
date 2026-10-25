# 23 — Union Find (Disjoint Set Union)

> Phase 8 · Roadmap Days 146–150 · Folder: `23-union-find/`

Two arrays and two rules — connect components and ask "are these connected?"
in near-constant time.

## Purpose

Union-Find solves *dynamic connectivity*: merging groups as you process
edges, counting components, detecting cycles in undirected graphs, and
"islands merging" variants. It replaces repeated BFS with something simpler
and faster.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Parent array | each element points to a representative | write `find` with path compression |
| Union by rank/size | attach the shallower tree under the deeper | keep trees flat |
| Path compression | `find` rewires nodes to the root | explain why it's near `O(1)` |
| `α(n)` amortized | inverse Ackermann — effectively 4 | state the real bound honestly |
| Component count | decrement on successful union | count provinces / clusters |

## Key patterns

1. **Union edge by edge** — the connected check *is* the cycle check.
2. **Grid → id mapping** — `id = r * n + c`, then union with 4-neighbours.
3. **Kruskal's algorithm** — sort edges, add if it joins two components
   (minimum spanning tree).
4. **Rollback / offline variants** — noted as advanced, not required here.

## Complexity expectations

- `find`/`union`: `O(α(n)) ≈ O(1)` amortized after path compression + union by
  rank; `O(n)` space.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | Medium | components over an adjacency matrix |
| 2 | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | cycle detection via union |
| 3 | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | union by key, then gather groups |

## Prerequisites and follow-ups

- **Before this:** `19-graphs` (motivation), `16-trees` (tree shape).
- **Next:** `20-greedy` — start Phase 9 (Kruskal is a greedy algorithm).

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
