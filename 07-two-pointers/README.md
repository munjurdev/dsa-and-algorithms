# 07 — Two Pointers

> Phase 3 · Roadmap Days 047–053 · Folder: `07-two-pointers/`

Two indices that move with a purpose — usually on a **sorted** array or
string — collapsing `O(n^2)` pair searches into a single `O(n)` pass.

## Purpose

Pair/triplet sums, in-place partitioning, palindromes, and container-style
maxima all reduce to: compare the two ends, move the one that can't be part
of the answer. It is the cheapest big win in most people's toolkit.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Left/right pointers | Start at both ends, converge | 3Sum, container-with-most-water |
| Fast/slow (runner) | One advances faster | find cycle, find middle in `O(1)` space |
| Same-direction pointers | Both advance, one lags | remove duplicates in place, partitions |
| Convergence proof | Show pointers never skip the answer | justify `O(n)` correctness |

## Key patterns

1. **Sorted + "too small/too large" → move left/right** accordingly.
2. **Partition in place** — slow pointer marks the write position.
3. **Expand from center** — palindrome detection (a two-pointer variant on
   a single string).

## Complexity expectations

- `O(n)` time for one pass (or `O(n^2)` for the classic all-pairs loop);
  `O(1)` extra space unless sorting counts against you (`O(n log n)` total
  with Python's sort).

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | Two Sum II – Input Array Is Sorted | Medium | converge on a sorted array |
| 2 | [3Sum](https://leetcode.com/problems/3sum/) | Medium | sort + fix one + two pointers |
| 3 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | greedy pointer movement |

## Prerequisites and follow-ups

- **Before this:** `06-hashing`, `05-sorting`.
- **Next:** `08-prefix-sum`, `09-sliding-window`.

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
