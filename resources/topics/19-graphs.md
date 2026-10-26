# 19 — Graphs

> Phase 8 · Roadmap: see `ROADMAP.md` · File: `resources/topics/19-graphs.md`

Arbitrary connections between nodes: the general case that everything else
was a special case of. Graph algorithms are about *traversal discipline*,
not memorized code.

## Purpose

Social networks, maps, dependencies, mazes, compilers — anything "linked
messily" is a graph. This is usually where interview preparation either
clicks (two traversals + topological sort cover most problems) or stalls, so
it gets the largest block of days.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Adjacency list vs matrix | list for sparse, matrix for dense | pick by `V`/`E` density |
| Directed vs undirected | one-way vs two-way edges | build edges correctly |
| BFS | frontier queue, `O(V + E)` | shortest path in an unweighted graph |
| DFS | recursion or explicit stack | components, cycles, connectivity |
| Visited discipline | mark on enqueue in BFS; handle gray/black | avoid double-counting and infinite loops |
| Topological order | ordering of a DAG | Kahn's algorithm with in-degrees |
| Weighted graphs | edges carry cost | Dijkstra (heaps), Bellman-Ford |

## Key patterns

1. **Grid as a graph** — each cell is a node, 4 directions are edges (islands,
   rotting oranges).
2. **Kahn's algorithm** — queue of in-degree-0 nodes; empty queue with nodes
   left ⇒ cycle.
3. **Multi-source BFS** — push all sources at once for "distance to nearest X."
4. **Dijkstra with a heap** — `(dist, node)` tuples, lazy deletion of stale
   entries.
5. **Connected components** — DFS/BFS flood fill, counting seeds.

## Complexity expectations

- Traversals: `O(V + E)` time, `O(V)` space.
- Dijkstra with a binary heap: `O((V + E) log V)`.
- Floyd-Warshall: `O(V^3)` — only for dense all-pairs.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | grid DFS/BFS components |
| 2 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | topological sort / cycle detection |
| 3 | Word Ladder | Hard | BFS on an implicit graph |

## Prerequisites and follow-ups

- **Before this:** `13-queue-and-deque` (BFS queue), `16-trees` (DFS
  intuition), `18-heaps` (for weighted shortest paths).
- **Next:** `23-union-find` (dynamic connectivity, closes Phase 8).

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
