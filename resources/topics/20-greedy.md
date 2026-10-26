# 20 — Greedy

> Phase 9 · Roadmap: see `ROADMAP.md` · File: `resources/topics/20-greedy.md`

Make the locally optimal choice *now* and never look back — when you can
prove that doing so cannot hurt the global answer.

## Purpose

Greedy algorithms are the fastest intuition builders for scheduling,
interval, and resource-allocation problems, and a useful contrast class that
makes dynamic programming clearer: greedy never revisits a decision; DP
keeps the states a greedy choice might regret.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Greedy choice property | a local optimum extends to a global one | state the argument in 1-2 sentences |
| Optimal substructure | the rest of the problem is the same, smaller | show why the choice doesn't break it |
| Exchange argument | swap any optimal solution toward yours | the standard proof technique |
| Sort-then-choose | order candidates, take the best-looking | interval scheduling, task assignment |
| Counterexample discipline | one bad case kills a greedy claim | find it before coding |

## Key patterns

1. **Earliest deadline / latest start** — sort intervals, iterate.
2. **Take while it fits** — assign cookies/slots greedily against remaining
   need.
3. **Always-positive gain first** — take items with the best ratio or the
   only non-negative effect (with care).
4. **Buy low, track minimum** — running-best stock-style scans.

## Complexity expectations

- Typically `O(n log n)` from sorting plus an `O(n)` scan; `O(1)`–`O(n)`
  extra space.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Easy | sort + two pointers greed |
| 2 | [Jump Game](https://leetcode.com/problems/jump-game/) | Medium | reachability greedy |
| 3 | Gas Station | Medium | circular greedy with proof |

## Prerequisites and follow-ups

- **Before this:** `05-sorting`, `23-union-find` (Kruskal is greedy).
- **Next:** `21-dynamic-programming` — where greedy falls short.

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
