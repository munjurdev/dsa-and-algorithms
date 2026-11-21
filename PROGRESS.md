# Progress Tracker

> **Status: Day 15 of 30 complete.** Phases 1–5 are done, weekly checkpoints 01
> and 02 and mock interview #1 are recorded, and Day 16 opens Phase 6. Update
> this file manually after each study session — honesty here is what makes the
> tracker useful.

## Run constants

| Field | Value |
|---|---|
| Start date | `2026-11-01` |
| Target completion date | `2026-12-01` _(start date + 30 practice days)_ |
| Total roadmap days | **30** |
| Completed days | **15 / 30** |
| Completed phases | **5 / 10** |

## Overall counters

Update these after each session.

| Metric | Count |
|---|---|
| Problems solved | 29 |
| — Easy | 12 |
| — Medium | 15 |
| — Hard | 2 |
| Revision reviews done | 5 |
| Mock interviews completed | 1 |
| Timed practice sessions | 2 |

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
- [x] 08 Prefix Sum
- [x] 09 Sliding Window
- [x] 10 Binary Search
- [x] 11 Linked List
- [x] 12 Stack
- [x] 13 Queue and Deque
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
| 13 Queue and Deque | 2026-11-21 | 2026-11-22 | Mock #1: `list.pop(0)` cost and the two-stack amortized argument need a re-derive; monotonic deque expiry order cost a hint |

## Phase checklist

| Phase | Days | Status |
|---|---|---|
| 1 — Python Fundamentals and Complexity Analysis | 01–03 | Complete |
| 2 — Arrays, Strings, Matrices, and Sorting | 04–06 | Complete |
| 3 — Hashing, Two Pointers, and Prefix Sums | 07–09 | Complete |
| 4 — Sliding Window and Binary Search | 10–12 | Complete |
| 5 — Linked Lists, Stacks, and Queues | 13–15 | Complete |
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
| 09 | 2026-11-10 | `08-prefix-sum` | [x] | [x] | [x] | Subarray Sum Equals K (empty prefix seeded, counts not overwrites); Product of Array Except Self (prefix/suffix, no division, O(1) extra space) |
| 10 | 2026-11-11 | `09-sliding-window` | [x] | [x] | [x] | Longest Substring Without Repeating Characters (left jumps past the repeat, never rewinds); Maximum Average Subarray I (k-sum slide, best seeded from the first window) |
| 11 | 2026-11-15 | `09-sliding-window` | [x] | [x] | [x] | Minimum Window Substring (need/surplus counts, repeated requirements worked); Find All Anagrams in a String (fixed-width counter equality, overlapping matches) |
| 12 | 2026-11-18 | `10-binary-search` | [x] | [x] | [x] | Search in Rotated Sorted Array (sorted-half test, exhaustive rotation differential check); Koko Eating Bananas (monotone `Σ ⌈p/k⌉ ≤ h` predicate, ceiling division and `hi = mid` bounds checked) |
| 13 | 2026-11-18 | `11-linked-list` | [x] | [x] | [x] | Reverse Linked List (iterative + recursive, in-place node identity asserted); Linked List Cycle (Floyd, identity not value comparison, visited-set differential check) |
| 14 | 2026-11-19 | `12-stack` | [x] | [x] | [x] | Valid Parentheses (stack + closer map, erase-pairs oracle over all 55,987 strings up to length 6); checkpoint 02: 3/3 closed-notes re-solves (Container With Most Water, Find All Anagrams, Search in Rotated Sorted Array) + `list.pop(0)` is O(n) — measured 4× growth per doubling |
| 15 | 2026-11-21 | `13-queue-and-deque` | [x] | [x] | [x] | Implement Queue using Stacks (two-stack amortized O(1), deque differential check, transfers counted); Sliding Window Maximum (monotonic deque, O(n), brute-force differential + full-size monotone shapes); mock interview #1 — 4/4 solved, transcript and weak areas in the mock log |
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
| 2 | 08–14 | Checkpoint 02 closed 3/3 from blank files; every re-solve was checked against an independent oracle (brute force, sorted-window, exhaustive rotations) instead of remembered examples; structural costs were measured rather than asserted | The anagram window has two traps a rebuilt-from-blank version can fall into — stepping by `len(p)` (drops overlapping matches) and re-counting each window (turns O(n) into O(n·m)); the container's discard proof needed re-deriving before the pointer rule felt justified | None from checkpoint 02 (3/3 re-derived); Day 11/12 anagram and rotated-search re-solves stay due on their recorded spaced-review dates | Day 15 mock interview #1 (queue/deque + stack), thinking aloud with a complexity defense |
| 3 | 15–21 | | | | |
| 4 | 22–28 | | | | |
| 5 | 29–30 | | | | |

## Mock interview log

The format is `ROADMAP.md` Appendix A: read the statement aloud, state the
approach and its complexity **before** coding, implement, run your own test
cases, then defend the complexity. One screen, no notes, 60 minutes total with
the wrap-up at minute 55.

### Mock interview #1 — 2026-11-21 (linked list + stack/queue)

| # | Problem | Topic | Time | Outcome |
|---|---|---|---|---|
| 1 | Reverse Linked List (Day 13 re-solve) | `11-linked-list` | 8 min | solved; wrote the node-identity assertion before the value test |
| 2 | Linked List Cycle (Day 13 re-solve) | `11-linked-list` | 11 min | solved with Floyd; coded before stating the bound (feedback) |
| 3 | Implement Queue using Stacks (Day 15) | `13-queue-and-deque` | 16 min | solved; called `pop` O(n) flat until asked for the amortized bound |
| 4 | Sliding Window Maximum (Day 15) | `13-queue-and-deque` | 20 min | O(n·k) re-scan first; monotonic deque after a hint about expiry order |
| — | Complexity defense / wrap-up | | 5 min | 3 of 4 defended without prompting |

**Transcript (condensed, in interview order).**

*Q1 — Reverse Linked List.* "I'll keep `prev = None`, `curr = head`, and save
`nxt` before rewiring `curr.next = prev`, so the unprocessed tail is never
lost." Follow-up: "Why not the recursive version for the 5000-node limit?" →
"It is O(n) stack frames and Python's default limit is 1000, so I'd use the
iterative one; the recursive form is the same invariant read backwards."

*Q2 — Linked List Cycle.* First answer: "I'd walk the list with a `set` of
visited nodes." Follow-up: "That is O(n) space — can you do better?" → Floyd,
slow and fast pointers. Follow-up: "Why must they meet if there is a cycle?"
(one prompt) → "Inside the cycle the gap shrinks by one per fast step, so it
reaches zero." Feedback: on this question I started coding before saying the
O(n)/O(1) bound.

*Q3 — Implement Queue using Stacks.* "Two stacks: push onto `inbox`; on
`pop`/`peek`, if `outbox` is empty, reverse `inbox` into it and pop from there."
I first said `pop` is O(n). Follow-up: "Worst case, or something else?" →
"Amortized O(1) — each element crosses the two stacks at most once, so any
sequence of n operations is O(n)." I tested `push 1, push 2, pop, push 3` to
show 3 queues behind 2.

*Q4 — Sliding Window Maximum.* First version recomputed `max(nums[i:i+k])`,
which is O(n·k). Follow-up: "Which candidates do you actually need?" → keep a
decreasing deque of indices. In my first deque version I read the front before
evicting the expired index, so the output was wrong; my own test
`[1,-1,-1], k = 2` caught it. Fixing the order to "pop smaller from the back,
append, evict expired front, then read" passed. Defense: each index is
appended once and removed at most once, so the scan is O(n) with O(k) space.

**Weak areas from this session**

| Weak area | Evidence | Fix / action | Next check |
|---|---|---|---|
| Amortized vs worst-case wording | Q3: stated a flat O(n) `pop` | Say the total bound out loud ("n operations cost O(n) because each element transfers once") before the per-call claim | `13-queue-and-deque`, 2026-11-22 |
| Monotonic-deque step order | Q4: read front before evicting the expired index | Evict expired front, *then* read; keep `[1,-1,-1], k = 2` as the regression case | `13-queue-and-deque`, 2026-11-22 |
| Approach before code | Q2: coded before stating complexity | 30-second approach + complexity statement before the first line, every timed session | Mock #2, Day 30 |
| Floyd termination proof | Q2: needed one prompt | State "gap shrinks by one per iteration, so it hits zero" as part of the solution | `11-linked-list`, 2026-11-25 |

The Day 15 solutions in `day-15/` are the cleaned-up versions of Q3 and Q4
written after the session; Q2/Q3/Q4's corrected steps are the ones recorded
above, not the first attempts.

## Rules for this file

1. Never mark a day complete in advance.
2. Count a problem only if you wrote the solution yourself and can re-derive
   the approach from a blank file.
3. Reset a counter honestly if a later review shows the concept did not stick.
