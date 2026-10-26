# 21 — Dynamic Programming

> Phase 9 · Roadmap: see `ROADMAP.md` · File: `resources/topics/21-dynamic-programming.md`

Recursion plus memoization: stop recomputing overlapping subproblems and you
turn exponential search into linear or quadratic time.

## Purpose

DP is the hardest standard interview topic because it is a *method for
inventing* algorithms, not one algorithm. The roadmap therefore spends its
biggest block here: derive the recurrence first, choose memo (recursive) or
tabulation (iterative) second, optimize space last.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Overlapping subproblems | the same state is reached many times | spot recomputation in a naive recursion |
| Optimal substructure | optimum is built from optima of subproblems | decide min/max/count vs yes/no |
| State definition | `dp[i]` must mean something precise | write the meaning before the transition |
| Transition | how `dp[i]` relates to earlier states | derive it from the recurrence |
| Base cases | smallest states, set directly | get off-by-ones right |
| Space optimization | only the previous row/variable is needed | reduce 2-D to 1-D when rows don't chain |

## Key patterns

1. **1-D linear DP** — climbing stairs, house robber, decode ways.
2. **Grid DP** — unique paths, minimum path sum.
3. **Knapsack 0/1** — capacity loop backwards; unbounded loop forwards.
4. **Interval / partition DP** — split points, `dp[i][j]`.
5. **String 2-D DP** — LCS, edit distance (two rows suffice).
6. **Subsequence over sequences** — LIS with patience sorting, `O(n log n)`.

## Complexity expectations

- States × transition cost. `n` states with `O(1)` transition → `O(n)`; a
  2-D table → `O(n·m)`; partition DP → `O(n^3)`.
- Space: table size, reducible when transitions only touch the previous row.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | first memo |
| 2 | [Coin Change](https://leetcode.com/problems/coin-change/) | Medium | unbounded knapsack, min count |
| 3 | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | 2-D string DP |

## Prerequisites and follow-ups

- **Before this:** `14-recursion` (recurrences), `20-greedy` (knowing when
  greedy fails).
- **Next:** `22-trie` — start Phase 10 (advanced topics and revision).

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
