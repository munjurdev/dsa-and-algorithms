# 25 — Intervals

> Phase 10 · Roadmap Days 174–175 · Folder: `25-intervals/`

Ranges `[start, end)` and the operations that combine, intersect, and schedule
them — sorting plus a linear scan does most of the work.

## Purpose

Calendar merging, room allocation, coverage, and overlap counting all reduce
to the same few moves: sort by one endpoint, sweep, and merge when a range
still touches the active one. This topic also introduces the **sweep line**,
which generalizes to counting problems far beyond intervals.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Closed vs half-open | `[a, b)` vs `[a, b]` affects touching ranges | pick one convention and state it |
| Sort by start | overlapping intervals become adjacent | merge in one pass |
| Sort by end | greedy non-overlap selection | maximum number of non-overlapping |
| Sweep line | `+1` at entry, `-1` at exit, track the max | count overlapping at any point |
| Interval insertion | split/trim existing ranges | insert a new interval correctly |

## Key patterns

1. **Merge** — sort by start, extend `cur_end` while the next overlaps.
2. **Insert** — keep intervals ending before the new one, merge the middle,
   append the rest.
3. **Sweep events** — endpoints as `(+1, -1)` events sorted with tie-break
   rules (process exits before entries when needed).
4. **Difference array** — `+v` / `-v` range updates (bridge back to
   `08-prefix-sum`).

## Complexity expectations

- `O(n log n)` dominated by sorting; `O(n)` scan; `O(n)` space for the output
  or the sweep's counter.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | sort by start, linear merge |
| 2 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | three-region split without overlap logic soup |
| 3 | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | sort by end, greedy removal |

## Prerequisites and follow-ups

- **Before this:** `05-sorting`, `07-two-pointers`, `20-greedy`.
- **Next:** `26-advanced-algorithms`.

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
