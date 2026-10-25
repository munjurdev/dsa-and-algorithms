# 08 — Prefix Sum

> Phase 3 · Roadmap Days 054–060 · Folder: `08-prefix-sum/`

Precompute cumulative values once so that thousands of range queries each
cost `O(1)` — the move that turns "too slow" into "trivial."

## Purpose

Subarray sums, range queries, and "count subarrays equal to k" all become
cheap once you store running totals. Prefix sums are also the mental seed of
dynamic programming (build on previous answers).

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| 1-D prefix array | `pref[i] = sum(nums[:i])` | answer `sum(nums[i:j])` in `O(1)` |
| Range sum | `pref[j] - pref[i]` | handle inclusive/exclusive indices exactly |
| Difference array | `+v` at `start`, `-v` at `end+1` | apply many range updates in `O(1)` |
| 2-D prefix | Integral image over a grid | any rectangle sum in `O(1)` |
| Prefix + hash map | count of each prefix value seen | subarray-sum-equals-k in `O(n)` |

## Key patterns

1. **Compute prefix, query with subtraction** — standard range sum.
2. **Map prefix → count while scanning** — number of subarrays with a target
   sum (the k = 0 variant uses the empty prefix as 1).
3. **Sort + prefix** — cumulative cost problems (buying minimum items, etc.).

## Complexity expectations

- Preprocess `O(n)`, query `O(1)` (2-D: `O(m·n)` preprocess).
- Scanning with a prefix map: `O(n)` time, `O(n)` space.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | Range Sum Query – Immutable | Easy | 1-D prefix array |
| 2 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | prefix + frequency map |
| 3 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | prefix/suffix products, no division |

## Prerequisites and follow-ups

- **Before this:** `06-hashing`, `07-two-pointers`.
- **Next:** `09-sliding-window` (a window whose sum you maintain incrementally).

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
