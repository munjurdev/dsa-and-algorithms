# 30-Day DSA Learning Roadmap

Day **01** through Day **30**, one row per day. Nothing in this file or in
[`PROGRESS.md`](PROGRESS.md) is pre-marked as complete — you fill those in as
you go.

## How to read this roadmap

Each day has six fields:

| Field | Meaning |
|---|---|
| **Day** | Matches the folder `day-NN/` where the day's work lives |
| **Topics** | The topic write-ups in [`resources/topics/`](resources/topics/) for the day |
| **Focus** | The specific idea you are learning today |
| **dsa/ problem** | The data-structure problem → `day-NN/dsa/problem.md` + `solution.py` |
| **algorithms/ problem** | The algorithm exercise → `day-NN/algorithms/problem.md` + `solution.py` |
| **Completion criterion** | An observable, checkable condition — the day is "done" only when this holds |

**Links policy:** links are given only for well-known problems whose LeetCode
slug is stable (`leetcode.com/problems/<slug>/`). For anything where a URL is
uncertain, the problem is named without a link rather than guessed. Verify
before relying on one.

## Scheduling rules built into this roadmap

- **Weekly checkpoints** — Days 007, 014, 021, and 028 are timed, closed-notes
  re-solves of the material behind you; each keeps one track for new material
  and devotes the other to the re-solve.
- **Mock interviews** — Day 015 (mid-point) and Day 030 (final): one timed
  session each, thinking aloud, ending with a complexity defense.
- **Phase boundaries** — every phase is exactly 3 days, so consolidation is
  built in at Days 003, 006, 009, 012, 015, 018, 021, 024, 027, 030.
- **Revision strategy** — re-solve a problem 1 day, 7 days, and 30 days after
  first solving it (record dates in `problem.md`'s *Review date* field).
- **Prerequisites** — no topic appears before the phase that introduces it.

## Phase overview

| Phase | Days | Topics | Days count |
|---|---|---|---|
| 1 — Python Fundamentals and Complexity Analysis | 01–03 | `00`, `01` | 3 |
| 2 — Arrays, Strings, Matrices, and Sorting | 04–06 | `02`, `03`, `04`, `05` | 3 |
| 3 — Hashing, Two Pointers, and Prefix Sums | 07–09 | `06`, `07`, `08` | 3 |
| 4 — Sliding Window and Binary Search | 10–12 | `09`, `10` | 3 |
| 5 — Linked Lists, Stacks, and Queues | 13–15 | `11`, `12`, `13` | 3 |
| 6 — Recursion and Backtracking | 16–18 | `14`, `15` | 3 |
| 7 — Trees, BSTs, Heaps, and Priority Queues | 19–21 | `16`, `17`, `18` | 3 |
| 8 — Graphs and Graph Algorithms | 22–24 | `19`, `23` | 3 |
| 9 — Greedy Algorithms and Dynamic Programming | 25–27 | `20`, `21` | 3 |
| 10 — Advanced Topics, Mixed Practice, and Interview Revision | 28–30 | `22`, `24`, `25`, `26`, `27` | 3 |
| **Total** | **01–30** | | **30** |

**Problem volume:** two problems or exercises per day (one per track), so the
roadmap lands at ~60 problems in total — with re-solves of your weakest ones
counted separately. Understanding beats count: a problem you can re-derive
from a blank file counts; one you copied does not.

---

## Phase 1 — Python Fundamentals and Complexity Analysis (Days 01–03)

| Day | Topics | Focus | dsa/ problem | algorithms/ problem | Completion criterion |
|---|---|---|---|---|---|
| 01 | `00-python-fundamentals` | Toolchain, variables, basic types, iteration toolkit | Reverse Words in a String (LeetCode, no link given) — Easy | FizzBuzz + top-k frequency drill (self-made) — Easy | Script runs clean; you can name the type of every variable used |
| 02 | `00-python-fundamentals` | Dicts, sets, comprehensions, pure typed functions | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) — Easy | Word-frequency analyzer capstone (self-made) — Medium | Frequencies correct in one pass; every function typed and pure |
| 03 | `01-complexity-analysis` | Big-O growth rates, loop analysis, amortized and space cost | Constraint range → allowed complexity mapping (self-made) — Medium | Classify 10 snippets + justify `list.append` amortization (self-made) — Easy | 10/10 correct, each with a one-line justification |

## Phase 2 — Arrays, Strings, Matrices, and Sorting (Days 04–06)

| Day | Topics | Focus | dsa/ problem | algorithms/ problem | Completion criterion |
|---|---|---|---|---|---|
| 04 | `02-arrays` | Single pass, running state, in-place compaction | [Two Sum](https://leetcode.com/problems/two-sum/) — Easy | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) — Medium | `O(n)` hash solution stated; Kadane correct including the all-negative case |
| 05 | `03-strings`, `04-matrices` | Palindrome checks; grid indexing and layer traversal | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) — Easy | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) — Medium | Correct on 1×n, n×1, and square boards; both palindrome variants agree |
| 06 | `05-sorting` | Sort from scratch; sort-then-scan | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) — Medium | Merge sort vs `sorted()` with randomized differential tests (self-made) — Medium | Touching intervals merged; merge sort passes randomized tests, `O(n log n)` derived |

## Phase 3 — Hashing, Two Pointers, and Prefix Sums (Days 07–09)

| Day | Topics | Focus | dsa/ problem | algorithms/ problem | Completion criterion |
|---|---|---|---|---|---|
| 07 | `06-hashing` | **Weekly checkpoint 01** — one-pass hashing, sets | [Two Sum](https://leetcode.com/problems/two-sum/) with a `value → index` map — Easy | Timed re-solve of 4 problems from Days 01–06, closed notes — Easy | `O(n)` solution; ≥ 4 of 5 re-derived without opening old code |
| 08 | `07-two-pointers` | Converging pointers, fix-one-then-scan, greedy movement | [3Sum](https://leetcode.com/problems/3sum/) — Medium | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) — Medium | No duplicate triplets; "move the smaller side" argument written down |
| 09 | `08-prefix-sum` | 1-D prefix array; prefix + hash map subarray counting | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) — Medium | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) — Medium | Empty-prefix case handled; `O(n)` with no division, `O(1)` extra space |

## Phase 4 — Sliding Window and Binary Search (Days 10–12)

| Day | Topics | Focus | dsa/ problem | algorithms/ problem | Completion criterion |
|---|---|---|---|---|---|
| 10 | `09-sliding-window` | Window invariant; expand then shrink | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) — Medium | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) — Easy | Invariant stated in one sentence; `O(n)` for both |
| 11 | `09-sliding-window` | need/have minimal window; anagram windows | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) — Hard | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) — Medium | Correct with repeated required characters; all start indices found |
| 12 | `10-binary-search` | The template and its invariants; binary search on the answer | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) — Medium | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) — Medium | Passes all 5 edge tests; monotone predicate written down |

## Phase 5 — Linked Lists, Stacks, and Queues (Days 13–15)

| Day | Topics | Focus | dsa/ problem | algorithms/ problem | Completion criterion |
|---|---|---|---|---|---|
| 13 | `11-linked-list` | Node, dummy head, fast/slow pointers | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) — Easy | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) — Easy | Iterative and recursive versions correct; Floyd is `O(n)` time, `O(1)` space |
| 14 | `12-stack` | **Weekly checkpoint 02** — LIFO matching, monotonic stack | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) — Easy | Timed re-solve of 3 problems from Days 08–13 + why `list.pop(0)` is `O(n)` — Medium | 3/3 rebuilt from blank files; each stack solution's amortized cost stated |
| 15 | `13-queue-and-deque` | Queue semantics, monotonic deque — **mock interview #1** | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) — Easy | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) — Hard | Mock finished; transcript and weak areas recorded in `PROGRESS.md` |

## Phase 6 — Recursion and Backtracking (Days 16–18)

| Day | Topics | Focus | dsa/ problem | algorithms/ problem | Completion criterion |
|---|---|---|---|---|---|
| 16 | `14-recursion` | Base case, recursive case, memoization | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (memoized) — Easy | Recursive merge sort vs `sorted()` (self-made) — Medium | `O(2^n)` before and `O(n)` after stated; output matches `sorted()` |
| 17 | `15-backtracking` | Choose → explore → un-choose | [Permutations](https://leetcode.com/problems/permutations/) — Medium | [Combination Sum](https://leetcode.com/problems/combination-sum/) — Medium | All outputs produced; undo step verified by a written trace |
| 18 | `15-backtracking` | Pruning and constraint propagation | [Subsets](https://leetcode.com/problems/subsets/) — Medium | [N-Queens](https://leetcode.com/problems/n-queens/) — Hard | All `2^n` subsets; all solutions found with the pruning rule stated |

## Phase 7 — Trees, BSTs, Heaps, and Priority Queues (Days 19–21)

| Day | Topics | Focus | dsa/ problem | algorithms/ problem | Completion criterion |
|---|---|---|---|---|---|
| 19 | `16-trees` | DFS orders, BFS level order, aggregation in one DFS | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) — Medium | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) — Easy | Levels returned as separate lists; diameter in one traversal, `O(n)` |
| 20 | `17-binary-search-tree` | The BST invariant, bounds validation, in-order streaming | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) — Medium | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) — Medium | Equal-value violations caught; `O(h + k)` correct when `k = n` |
| 21 | `18-heaps-and-priority-queue` | **Weekly checkpoint 03** — heap mechanics, top-k | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) — Medium | Timed re-solve of 3 problems from Days 15–20, closed notes — Medium | Size-k heap with `O(n log k)` stated; 3/3 re-solves without notes |

## Phase 8 — Graphs and Graph Algorithms (Days 22–24)

| Day | Topics | Focus | dsa/ problem | algorithms/ problem | Completion criterion |
|---|---|---|---|---|---|
| 22 | `19-graphs` | Representations, BFS/DFS, grid as a graph | [Number of Islands](https://leetcode.com/problems/number-of-islands/) — Medium | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) — Medium | All islands found, `O(mn)`; impossible case returns −1 |
| 23 | `19-graphs` | Cycle detection, topological sort, Dijkstra | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) — Medium | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) — Medium | Valid order or `[]` on a cycle; `O(E log V)` with stale heap entries skipped |
| 24 | `23-union-find` | DSU: find, union, rank; Kruskal's MST | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) — Medium | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) — Medium | Component count correct, `α(n)` explained; `O(E log E)` stated |

## Phase 9 — Greedy Algorithms and Dynamic Programming (Days 25–27)

| Day | Topics | Focus | dsa/ problem | algorithms/ problem | Completion criterion |
|---|---|---|---|---|---|
| 25 | `20-greedy` | Greedy choice property; exchange argument | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) — Medium | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) — Medium | Proof written **before** the code; correct minimum count |
| 26 | `21-dynamic-programming` | State → transition → base case; linear and 0/1 knapsack DP | [House Robber](https://leetcode.com/problems/house-robber/) — Medium | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) — Medium | Correct for `n = 1` and `n = 2`; `O(n · cap)` with the subset reconstructable |
| 27 | `21-dynamic-programming` | Unbounded knapsack, subsequence DP, two complexities | [Coin Change](https://leetcode.com/problems/coin-change/) — Medium | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) — Medium | Impossible case returns −1; both `O(n²)` and `O(n log n)` work and are stated |

## Phase 10 — Advanced Topics, Mixed Practice, and Interview Revision (Days 28–30)

| Day | Topics | Focus | dsa/ problem | algorithms/ problem | Completion criterion |
|---|---|---|---|---|---|
| 28 | `22-trie`, `24-bit-manipulation` | **Weekly checkpoint 04** — trie, bit masks | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) — Medium | Timed re-solve of 3 problems from Days 22–27 + subset-mask drill — Medium | All trie operations correct; bitmask enumeration matches brute force; 3/3 re-solves |
| 29 | `25-intervals`, `26-advanced-algorithms` | Interval sweep; advanced overview (Floyd–Warshall, rolling hash) | [Insert Interval](https://leetcode.com/problems/insert-interval/) — Medium | Rabin–Karp vs naive substring search (self-made) — Hard | All overlap cases correct; rolling hash matches naive on randomized tests, collision risk stated |
| 30 | `27-patterns-and-revision` | Pattern identification under time pressure — **final mock + retrospective** | Mock set: 1 unseen medium from your weakest topic (self-made) — Medium | Write the pattern sheet from memory, no code (self-made) — Medium | Mock completed; ≥ 8/8 patterns named in under 15 minutes; `PROGRESS.md` counters finalized honestly |

---

## Appendix A — Checkpoints and mocks

| Type | Day | Format |
|---|---|---|
| Weekly checkpoint 01 | 007 | Timed re-solve of Days 001–006, closed notes |
| Weekly checkpoint 02 | 014 | Timed re-solve of Days 008–013, closed notes |
| Weekly checkpoint 03 | 021 | Timed re-solve of Days 015–020, closed notes |
| Weekly checkpoint 04 | 028 | Timed re-solve of Days 022–027, closed notes |
| Mock interview #1 | 015 | 60 min, linked list + stack/queue, spoken aloud |
| Final mock + retrospective | 030 | 90 min, anything from the roadmap, then the write-up |

A mock session = read the statement aloud, state the approach and its
complexity **before** coding, implement, run your own test cases, then note
what you would do differently. Record it in `PROGRESS.md`.

## Appendix B — Revision strategy

1. **Spaced re-solves** — after first solving a problem, re-solve it on
   Day + 1, Day + 7, and Day + 30 (put the dates in `problem.md`'s
   *Review date* field).
2. **Weekly checkpoints** — Appendix A is the scheduled version of (1).
3. **Topic revision** — anything you could not re-derive goes into the
   *Topics requiring revision* table in `PROGRESS.md` with a next-review date.
4. **Day 30 is not the end** — loop the weak areas: pull every topic still
   unchecked in `PROGRESS.md`, keep one mock per week, and add a new
   `day-NN/` folder for each extra day you run.
