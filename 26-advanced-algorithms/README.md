# 26 — Advanced Algorithms

> Phase 10 · Roadmap Days 176–177 · Folder: `26-advanced-algorithms/`

Deliberately light: techniques worth *knowing about* and being able to
recognize, without pretending mastery after two days.

## Purpose

Exposure to heavier machinery — advanced graph, string, and optimization
techniques — so that if one shows up in an interview or contest, you know
what family it belongs to and where to study it properly.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Floyd–Warshall | all-pairs shortest paths, `O(V^3)` | set up the k-loop correctly |
| Bellman-Ford | shortest paths with negative edges | `V-1` relaxations + negative-cycle check |
| A* search | BFS/Dijkstra + heuristic | say when the heuristic must be admissible |
| String hashing / Rabin-Karp | rolling hash compares substrings `O(1)` | describe collision risk and the fallback |
| KMP-style matching | prefix function avoids re-scanning | explain the failure-function idea |
| Segment tree / BIT | range sum/query with updates, `O(log n)` | know when an array is not enough |
| Flow / matching (overview) | max-flow min-cut, bipartite matching | recognize the problem shape |

## Key patterns

1. **Recognize the family first** — "many range updates with point queries"
   → BIT/difference array; "many substring searches" → Rabin-Karp/KMP.
2. **Implement only what you've understood twice** — this phase is about
   *recognition*, and the roadmap depth follows.

## Complexity expectations

- Know each technique's complexity *and* the constraint range that makes it
  the right choice (e.g. `V ≤ 500` for Floyd–Warshall).

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | Dijkstra practice before Bellman-Ford |
| 2 | Find the City with the Smallest Number of Neighbors | Medium | Floyd–Warshall setup |
| 3 | KMP substring occurrence (implement yourself) | Hard | prefix function |

## Prerequisites and follow-ups

- **Before this:** `19-graphs`, `21-dynamic-programming`, `09-sliding-window`.
- **Next:** `27-patterns-and-revision` — consolidate everything.

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
