# Progress Tracker

> **Status: Day 08 of 30 complete.** Phases 1 and 2 are done and weekly
> checkpoint 01 passed; Day 09 continues Phase 3. Update this file manually
> after each study session — honesty here is what makes the tracker useful.

## Run constants

| Field | Value |
|---|---|
| Start date | `2026-11-01` |
| Target completion date | `2026-12-01` _(start date + 30 practice days)_ |
| Total roadmap days | **30** |
| Completed days | **8 / 30** |
| Completed phases | **2 / 10** |

## Overall counters

Update these after each session.

| Metric | Count |
|---|---|
| Problems solved | 15 |
| — Easy | 7 |
| — Medium | 8 |
| — Hard | 0 |
| Revision reviews done | 4 |
| Mock interviews completed | 0 |
| Timed practice sessions | 1 |

## Topics completed

Mark a topic when every assigned day for it is done **and** you can explain
its core patterns without notes. Topic write-ups live in
[`resources/topics/`](resources/topics/).

- [x] 00 Python Fundamentals
- [x] 01 Complexity Analysis
- [x] 02 Arrays
- [x] 03 Strings
- [x] 04 Matrices
- [x] 05 Sorting
- [x] 06 Hashing
- [x] 07 Two Pointers
- [ ] 08 Prefix Sum
- [ ] 09 Sliding Window
- [ ] 10 Binary Search
- [ ] 11 Linked List
- [ ] 12 Stack
- [ ] 13 Queue and Deque
- [ ] 14 Recursion
- [ ] 15 Backtracking
- [ ] 16 Trees
- [ ] 17 Binary Search Tree
- [ ] 18 Heaps and Priority Queue
- [ ] 19 Graphs
- [ ] 20 Greedy
- [ ] 21 Dynamic Programming
- [ ] 22 Trie
- [ ] 23 Union Find
- [ ] 24 Bit Manipulation
- [ ] 25 Intervals
- [ ] 26 Advanced Algorithms
- [ ] 27 Patterns and Revision

## Topics requiring revision

List anything that still feels shaky. Re-review before moving on.

| Topic | Last reviewed | Next review | Notes |
|---|---|---|---|
| _none yet_ | | | |

## Phase checklist

| Phase | Days | Status |
|---|---|---|
| 1 — Python Fundamentals and Complexity Analysis | 01–03 | Complete |
| 2 — Arrays, Strings, Matrices, and Sorting | 04–06 | Complete |
| 3 — Hashing, Two Pointers, and Prefix Sums | 07–09 | In progress — Day 08 done |
| 4 — Sliding Window and Binary Search | 10–12 | Not started |
| 5 — Linked Lists, Stacks, and Queues | 13–15 | Not started |
| 6 — Recursion and Backtracking | 16–18 | Not started |
| 7 — Trees, BSTs, Heaps, and Priority Queues | 19–21 | Not started |
| 8 — Graphs and Graph Algorithms | 22–24 | Not started |
| 9 — Greedy Algorithms and Dynamic Programming | 25–27 | Not started |
| 10 — Advanced Topics, Mixed Practice, and Interview Revision | 28–30 | Not started |

## Daily log

One row per study day. `Day` matches the folder `day-NN/`. Leave `Done?`
unchecked until both tracks (`dsa/` and `algorithms/`) meet the day's
completion criterion in [`ROADMAP.md`](ROADMAP.md).

| Day | Date | Topics | dsa/ done? | algorithms/ done? | Done? | Notes |
|---|---|---|---|---|---|---|
| 01 | 2026-11-01 | `00-python-fundamentals` | [x] | [x] | [x] | Reverse Words in a String; FizzBuzz + top-k frequency drill |
| 02 | 2026-11-01 | `00-python-fundamentals` | [x] | [x] | [x] | Valid Anagram; word-frequency analyzer (one pass, typed pure functions) |
| 03 | 2026-11-03 | `01-complexity-analysis` | [x] | [x] | [x] | Constraint range → allowed complexity map; 10 snippets classified |
| 04 | 2026-11-05 | `02-arrays` | [x] | [x] | [x] | Two Sum (hash, O(n)); Maximum Subarray (Kadane, all-negative case) |
| 05 | 2026-11-07 | `03-strings`, `04-matrices` | [x] | [x] | [x] | Valid Palindrome (both variants agree); Spiral Matrix (1×n and n×1 exact) |
| 06 | 2026-11-08 | `05-sorting` | [x] | [x] | [x] | Merge Intervals (touching merged); merge sort vs `sorted()`, `n·⌈log₂ n⌉` bound checked |
| 07 | 2026-11-09 | `06-hashing` | [x] | [x] | [x] | Two Sum re-derived from blank (value→index map, earliest pair); checkpoint 01: 4/4 closed-notes re-solves |
| 08 | 2026-11-10 | `07-two-pointers` | [x] | [x] | [x] | 3Sum (sort + fix one + skip duplicates, no repeated triplets); Container With Most Water (move the smaller side, differential-checked) |
| 09 | | | [ ] | [ ] | [ ] | |
| 10 | | | [ ] | [ ] | [ ] | |
| 11 | | | [ ] | [ ] | [ ] | |
| 12 | | | [ ] | [ ] | [ ] | |
| 13 | | | [ ] | [ ] | [ ] | |
| 14 | | | [ ] | [ ] | [ ] | |
| 15 | | | [ ] | [ ] | [ ] | |
| 16 | | | [ ] | [ ] | [ ] | |
| 17 | | | [ ] | [ ] | [ ] | |
| 18 | | | [ ] | [ ] | [ ] | |
| 19 | | | [ ] | [ ] | [ ] | |
| 20 | | | [ ] | [ ] | [ ] | |
| 21 | | | [ ] | [ ] | [ ] | |
| 22 | | | [ ] | [ ] | [ ] | |
| 23 | | | [ ] | [ ] | [ ] | |
| 24 | | | [ ] | [ ] | [ ] | |
| 25 | | | [ ] | [ ] | [ ] | |
| 26 | | | [ ] | [ ] | [ ] | |
| 27 | | | [ ] | [ ] | [ ] | |
| 28 | | | [ ] | [ ] | [ ] | |
| 29 | | | [ ] | [ ] | [ ] | |
| 30 | | | [ ] | [ ] | [ ] | |

## Weekly review log

Complete at each checkpoint (Days 007, 014, 021, 028) and at the end.

| Week | Days | What went well | What was hard | Revision needed | Plan for next week |
|---|---|---|---|---|---|
| 1 | 01–07 | Every day logged; hash-map pattern re-derived from a blank file; differential tests written for every solution instead of relying on remembered outputs | Spiral's single-row/single-column guards and interval nesting ends are the two details that had to be re-worked under time pressure | None from checkpoint 01 (4/4 re-derived); Day 04/05 spaced re-solves stay due on their recorded dates | Phase 3: two pointers on Day 08, prefix sums on Day 09, then sliding window |
| 2 | 08–14 | | | | |
| 3 | 15–21 | | | | |
| 4 | 22–28 | | | | |
| 5 | 29–30 | | | | |

## Rules for this file

1. Never mark a day complete in advance.
2. Count a problem only if you wrote the solution yourself and can re-derive
   the approach from a blank file.
3. Reset a counter honestly if a later review shows the concept did not stick.
