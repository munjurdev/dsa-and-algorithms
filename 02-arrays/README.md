# 02 — Arrays

> Phase 2 · Roadmap Days 016–024 · Folder: `02-arrays/`

Arrays are the most examined structure in interviews. Master indexing,
in-place updates, and the scan patterns every other topic builds on.

## Purpose

Most interview problems are "given an array, find/transform/arrange
something." Arrays teach the two foundational moves — **scan once** and
**reorder in place** — plus the `O(1)` random access model that makes binary
search and hashing possible later.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Random access | `nums[i]` in `O(1)` | reason about index bounds safely |
| Two-end traversal | Move from both ends or one direction | find pairs/conditions in one pass |
| In-place updates | `O(1)` extra space, write over the input | remove/rotate/dedupe without extra arrays |
| Prefix products/sums | Precompute to answer queries in `O(1)` | derive prefix sums unprompted |
| Kadane's algorithm | Running best-ending-here | solve max subarray in `O(n)` |

## Key patterns

1. **Single pass with a running state** — best, count, xor, accumulate.
2. **In-place compaction** — slow/fast write index (`move zeroes`, dedupe).
3. **Reversal algorithms** — rotate/merge without extra memory.
4. **Sort first, then scan** — when order unlocks the solution.

## Complexity expectations

- Target `O(n)` time for search/scan problems; `O(n log n)` when sorting is
  allowed; `O(n^2)` only for the brute-force baseline you then improve.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | hash map pass |
| 2 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | Kadane's algorithm |
| 3 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | in-place compaction |

## Prerequisites and follow-ups

- **Before this:** `00-python-fundamentals`, `01-complexity-analysis`.
- **Next:** `03-strings` (arrays of characters), then hashing, two pointers,
  prefix sums.

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
