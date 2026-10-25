# 180-Day DSA Learning Roadmap

Day **001** through Day **180**, one row per day. Nothing in this file or in
[`PROGRESS.md`](PROGRESS.md) is pre-marked as complete — you fill those in as
you go.

## How to read this roadmap

Each day has seven fields:

| Field | Meaning |
|---|---|
| **Day** | Day number, `001`–`180`, used as the filename prefix for your solutions |
| **Topic** | The topic folder where the day's work belongs |
| **Concept** | The specific idea you are learning today |
| **Practice task** | What you actually do with your hands |
| **Suggested problem** | A concrete problem to attempt (name + platform link where the URL is certain) |
| **Difficulty** | Of the suggested problem: Easy / Medium / Hard |
| **Completion criterion** | An observable, checkable condition — the day is "done" only when this holds |

**Links policy:** links are given only for well-known problems whose LeetCode
slug is stable (`leetcode.com/problems/<slug>/`). For anything where a URL is
uncertain, the problem is named without a link rather than guessed. Verify
before relying on one.

## Scheduling rules built into this roadmap

- **Weekly checkpoints** — every 7th day (007, 014, 021, …, 175) is a timed
  re-solve of that week's material, closed notes.
- **Mock interviews** — Days 040, 060, 096, 131, 168, and 180: one timed
  session, thinking aloud, ending with a complexity defense.
- **Phase checkpoints / buffer** — the last day of every phase doubles as
  review + catch-up; extra buffer days are marked inline (046, 090, 121,
  145, 177).
- **Revision strategy** — re-solve a problem 1 day, 7 days, and 30 days
  after first solving it (record dates in the solution docstring's
  *Review Date* field). Weekly checkpoints and the `27-patterns-and-revision`
  phase are the scheduled versions of this.
- **Prerequisites** — no topic appears before the phase that introduces it;
  hard problems are deferred until their prerequisites are covered.

## Phase overview

| Phase | Days | Topics | Days count |
|---|---|---|---|
| 1 — Python Fundamentals and Complexity Analysis | 001–015 | `00`, `01` | 15 |
| 2 — Arrays, Strings, Matrices, and Sorting | 016–040 | `02`, `03`, `04`, `05` | 25 |
| 3 — Hashing, Two Pointers, and Prefix Sums | 041–060 | `06`, `07`, `08` | 20 |
| 4 — Sliding Window and Binary Search | 061–078 | `09`, `10` | 18 |
| 5 — Linked Lists, Stacks, and Queues | 079–096 | `11`, `12`, `13` | 18 |
| 6 — Recursion and Backtracking | 097–112 | `14`, `15` | 16 |
| 7 — Trees, BSTs, Heaps, and Priority Queues | 113–131 | `16`, `17`, `18` | 19 |
| 8 — Graphs and Graph Algorithms | 132–150 | `19`, `23` | 19 |
| 9 — Greedy Algorithms and Dynamic Programming | 151–168 | `20`, `21` | 18 |
| 10 — Advanced Topics, Mixed Practice, and Interview Revision | 169–180 | `22`, `24`, `25`, `26`, `27` | 12 |
| **Total** | **001–180** | | **180** |

**Problem volume:** each day names one primary problem and weekly checkpoints
add 2–4 more per week, so the roadmap lands at roughly 200–260 problems in
total — with re-solves of your weakest ones counted separately. Understanding
beats count: a problem you can re-derive from a blank file counts; one you
copied does not.

---

## Phase 1 — Python Fundamentals and Complexity Analysis (Days 001–015)

### Days 001–007

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 001 | 00-python-fundamentals | Toolchain, variables, basic types, input/output | Create a venv; write a script that reads input, prints values with their `type()` | FizzBuzz (self-made) | Easy | Script runs clean; you can name the type of every variable used |
| 002 | 00-python-fundamentals | Strings: indexing, slicing, immutability | Do 10 slicing exercises; reverse a string 3 different ways | Reverse Words in a String (LeetCode, no link given) | Easy | All 10 slices correct; you can explain why `s[0] = "x"` fails |
| 003 | 00-python-fundamentals | Lists: append/insert/pop, list comprehensions | Rewrite 5 `for` loops as comprehensions | Remove Duplicates from Sorted Array (LeetCode, no link given) | Easy | Comprehensions produce identical output to the loops; in-place variant uses `O(1)` extra space |
| 004 | 00-python-fundamentals | Dicts and sets: membership, counting | Build a word-frequency counter over a paragraph | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Frequencies correct in one pass; you state the average `O(1)` lookup cost |
| 005 | 00-python-fundamentals | Functions: parameters, defaults, type hints, purity | Refactor Day 004 into typed pure functions | Self-made: `normalize(text) -> dict[str, int]` | Easy | All functions carry type hints; no mutable default arguments anywhere |
| 006 | 00-python-fundamentals | Iteration toolkit: `enumerate`, `zip`, `any/all`, `Counter`, `defaultdict` | 3 micro-drills, each requiring a specific tool | Self-made: top-k frequency without `heapq` | Easy | Each drill solved in ≤ 10 lines using the intended tool |
| 007 | 00-python-fundamentals | **Weekly checkpoint 01** — timed, closed notes | Re-solve Days 001–006 drills in 45 minutes | Timed review set (self-made) | Easy | ≥ 4 of 5 re-derived without looking at old code; gaps logged in `PROGRESS.md` |

### Days 008–014

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 008 | 00-python-fundamentals | Cost of built-ins; debugging with `assert` and `breakpoint()` | Add assert-based tests to your Day 004–006 scripts | Self-made: test suite for earlier functions | Easy | All asserts pass; you state the complexity of 3 built-ins correctly |
| 009 | 00-python-fundamentals | Mini-capstone: pull the phase together | Build a CLI word-frequency analyzer (read file → top-k words) | Capstone (self-made) | Medium | Runs end-to-end on a real text file; time and space complexity stated |
| 010 | 01-complexity-analysis | Big-O basics: growth rates, dropping constants | Classify 10 given snippets into `O(1)`…`O(2^n)` | Classify 10 snippets (self-made) | Easy | 10/10 correct, each with a one-line justification |
| 011 | 01-complexity-analysis | Loop analysis: nested, shrinking, and halving loops | Hand-count iterations for loops at `n = 1000` | Trace-the-loop exercises (self-made) | Easy | Correctly derive `O(n^2)`, `O(n log n)`, `O(log n)` for all exercises |
| 012 | 01-complexity-analysis | Best/average/worst case; amortized analysis | Write a paragraph justifying `list.append` as amortized `O(1)` | Written analysis (self-made) | Easy | Explanation includes the doubling-resize argument |
| 013 | 01-complexity-analysis | Space complexity and the recursion stack | Analyze space for 5 programs, one recursive | Analyze memo table vs recursion tree (self-made) | Easy | Correct space bound for each, including stack depth |
| 014 | 01-complexity-analysis | **Weekly checkpoint 02** — constraints → allowed complexity | Map constraint ranges (`n ≤ 10` … `n ≤ 10^7`) to allowed complexities | Constraint-mapping table (self-made) | Medium | All mappings correct; ≥ 4 include a named algorithm family |

### Days 015–024

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 015 | 01-complexity-analysis | **Phase 1 checkpoint / buffer** — written analysis test | 30-minute timed analysis test; re-attempt your weakest day | Mock analysis test (self-made) | Medium | Score ≥ 80%; weak areas recorded in `PROGRESS.md` |
| 016 | 02-arrays | Array anatomy: indexing, bounds, single scan | Trace indices on paper, then code a linear scan | [Two Sum](https://leetcode.com/problems/two-sum/) (brute force `O(n^2)`) | Easy | Finds all pairs; complexity stated as `O(n^2)` |
| 017 | 02-arrays | Running state in one pass: max, sum | Implement running max and running sum helpers | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | Correct on all tests including the all-negative case |
| 018 | 02-arrays | Two-pointer merge of sorted inputs | Merge two sorted arrays from the end | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Easy | Output sorted; `O(n + m)` stated |
| 019 | 02-arrays | In-place compaction with a write index | Remove elements with a slow pointer | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | In place, order preserved, `O(n)` time |
| 020 | 02-arrays | Rotation by reversal | Rotate without an extra array | [Rotate Array](https://leetcode.com/problems/rotate-array/) | Medium | Works for `k > n`; `O(1)` extra space |
| 021 | 02-arrays | **Weekly checkpoint 03** — voting and sort-assisted scans | Implement Boyer–Moore majority vote | [Majority Element](https://leetcode.com/problems/majority-element/) | Easy | `O(n)` time, `O(1)` space; you can explain why the count never breaks |
| 022 | 02-arrays | Index-as-hash trick | Mark visited indices, then read the result | [Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) | Medium | `O(n)` time, `O(1)` extra space (output excluded) |
| 023 | 02-arrays | Pattern mixing on arrays | Solve 3 varied array problems back-to-back | [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/) | Easy | 3/3 within 40 minutes |
| 024 | 02-arrays | Arrays capstone: unseen problems under time | 45-minute set: 1 unseen easy + 1 unseen medium | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Medium | Both solved within time; complexity written for each |

### Days 025–031

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 025 | 03-strings | Immutability cost; build strings with `join` | Rewrite concatenation-in-a-loop solutions using `join` | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | `O(n)` solution; you can say why `s += c` in a loop is quadratic |
| 026 | 03-strings | Palindrome checks: two pointers, expand-around-center | Implement palindrome check 2 ways | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Handles spaces/punctuation; both versions agree on all tests |
| 027 | 03-strings | Signature normalization for grouping | Group words by their sorted signature | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Correct grouping; complexity `O(n · k log k)` stated |
| 028 | 03-strings | **Weekly checkpoint 04** — timed strings set | 40-minute set: 1 easy + 1 medium, closed notes | Timed: [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | Finished within the time box; any gap logged for re-solve |
| 029 | 03-strings | Run-length encoding; round-trip testing | Implement encode and decode | Self-made: run-length encoder | Medium | `decode(encode(s)) == s` for a test battery including runs of 1 |
| 030 | 03-strings | String capstone: harder transform | Attempt one medium string problem unseen | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | Correct answer; expand-around-center complexity `O(n^2)` stated |
| 031 | 04-matrices | Grid indexing, direction arrays, boundary checks | Code the 4-neighbour walk; no index errors on 1×n grids | [Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy | Correct traversal on all board shapes |

### Days 032–040 — Matrices and sorting (Phase 2 close)

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 032 | 04-matrices | Layer traversal (peel the ring) | Implement spiral order | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | Correct for 1×n, n×1, and square boards |
| 033 | 04-matrices | In-place 2-D transform | Rotate a matrix 90° without extra memory | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | `O(1)` extra space; correct for odd-sized matrices |
| 034 | 04-matrices | Sentinel marking and restoration | Zero a matrix in `O(1)` space | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | Sentinel choice documented; matrix restored correctly |
| 035 | 05-sorting | **Weekly checkpoint 05** — Python sort: keys, stability, comparators | Sort records by two keys, both directions; then count-sort 3 values | [Sort Colors](https://leetcode.com/problems/sort-colors/) (counting solution) | Medium | Counting solution is `O(n)` and in place |
| 036 | 05-sorting | Merge sort from scratch | Implement merge sort; test stability | Self-made: merge sort vs `sorted()` | Medium | Passes randomized differential tests; `O(n log n)` derived |
| 037 | 05-sorting | Quick sort and partitioning | Implement Lomuto partition + quicksort | Self-made: compare pivot strategies | Medium | Correct on random, sorted, and duplicate-heavy inputs |
| 038 | 05-sorting | Sort-then-scan | Sort by a custom key, then a linear scan | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Correct merge including touching intervals |
| 039 | 05-sorting | Selection: sort vs heap vs quickselect | Solve once by sorting, once with a heap | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Two working solutions; complexities contrasted in writing |
| 040 | 05-sorting | **Mock interview #1 / Phase 2 checkpoint** | 60-minute mock: 3 problems across arrays, strings, sorting | Mock set (self-made) | Medium | Mock finished; transcript and weak areas recorded in `PROGRESS.md` |

---

## Phase 3 — Hashing, Two Pointers, and Prefix Sums (Days 041–060)

### Days 041–046 — Hashing

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 041 | 06-hashing | Hash map fundamentals; one-pass frequency map | Solve with a `value → index` map | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | `O(n)`; average vs worst case stated |
| 042 | 06-hashing | **Weekly checkpoint 06** — sets: dedupe and membership | Solve with set thinking, no sorting | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | `O(n)` time, `O(n)` space |
| 043 | 06-hashing | Cycle detection with a seen-set | Detect repeated states while transforming numbers | [Happy Number](https://leetcode.com/problems/happy-number/) | Easy | No infinite loop; terminates on repeat or on 1 |
| 044 | 06-hashing | Grouping with dictionary values | Re-derive anagram grouping without looking | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) (re-solve) | Medium | Re-derived within 25 minutes, no peeking |
| 045 | 06-hashing | Set-driven streaks | Find the longest run of consecutive numbers in `O(n)` | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | `O(n)` claimed and actually achieved |
| 046 | 06-hashing | **Buffer day** — catch up on 041–045, then a capstone | Re-attempt every failed problem from the week, then 1 unseen medium | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | All earlier failures re-solved cleanly; new problem in ≤ 25 min |

### Days 047–053 — Two pointers

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 047 | 07-two-pointers | Converging pointers on sorted input | Two-sum on a sorted array with no hash map | Two Sum II (name only — slug not verified) | Easy | `O(n)` time, `O(1)` space |
| 048 | 07-two-pointers | Fix one element, then two pointers | Find all unique triplets | [3Sum](https://leetcode.com/problems/3sum/) | Medium | No duplicate triplets; output sorted |
| 049 | 07-two-pointers | **Weekly checkpoint 07** | Timed re-solve of 3 problems from Days 041–048 | Review set (self-made) | Medium | 3/3 without notes |
| 050 | 07-two-pointers | Greedy pointer movement | Code it, then justify “move the smaller side” | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | `O(n)`; movement argument written in the docstring |
| 051 | 07-two-pointers | In-place partition | One-pass, constant-space sort of 3 colors | [Sort Colors](https://leetcode.com/problems/sort-colors/) (two-pointer redo) | Medium | Single pass; `O(1)` extra space |
| 052 | 07-two-pointers | One-deletion tolerance | Check palindrome allowing one skip | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | Easy | Correct on both skip branches; `O(n)` |
| 053 | 07-two-pointers | Two-pointer capstone | Unseen problem, 30-minute box | Boats to Save People (name only — link not verified) | Medium | Solved in time, or a documented attempt naming the missing insight |

### Days 054–060 — Prefix sums (Phase 3 close)

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 054 | 08-prefix-sum | 1-D prefix array; `O(1)` range query | Build a prefix array, answer 5 queries | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Easy | All queries correct in `O(1)` each |
| 055 | 08-prefix-sum | Running sums; pivot logic | Compute running sums; find the balance point | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Easy | Correct including the no-answer case |
| 056 | 08-prefix-sum | **Weekly checkpoint 08** | Timed: 2 review problems from Days 047–055 | Review set (self-made) | Medium | 2/2 within 40 minutes |
| 057 | 08-prefix-sum | Prefix + hash map: count subarrays | Count subarrays with sum `k` in `O(n)` | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | Empty-prefix case handled correctly |
| 058 | 08-prefix-sum | Difference array: range updates | Apply 1,000 range increments in `O(1)` each | Self-made: range-add drill | Medium | Final array correct; `O(n + q)` stated |
| 059 | 08-prefix-sum | Prefix products, 2-D prefix intuition | Solve without using division | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | `O(n)` time, no division, `O(1)` extra space |
| 060 | 08-prefix-sum | **Mock interview #2 / Phase 3 checkpoint** | 50-minute mock: 1 medium from this phase + 1 review problem, spoken aloud | Mock set (self-made) | Medium | Approach transcript written; logged in `PROGRESS.md` |

---

## Phase 4 — Sliding Window and Binary Search (Days 061–078)

### Days 061–069 — Sliding window

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 061 | 09-sliding-window | Window invariant; expand then shrink | Fixed-size window average | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | `O(n)`; invariant stated in one sentence |
| 062 | 09-sliding-window | Variable window with a seen map | Longest substring without repeats | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Correct on all repeated-character patterns |
| 063 | 09-sliding-window | **Weekly checkpoint 09** | Timed re-solve: prefix-sum + window problems | Review set (self-made) | Medium | 3/3 without notes |
| 064 | 09-sliding-window | Frequency-constrained window | Longest substring with limited replacements | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | Window validity explained, not guessed |
| 065 | 09-sliding-window | need/have minimal window | Shrink to the minimal covering window | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | Correct with multiple required characters and repeats |
| 066 | 09-sliding-window | “At most → exactly” counting | Count windows by ending position | Self-made: count subarrays with `max − min ≤ K` | Medium | Counts correct; `O(n)` stated |
| 067 | 09-sliding-window | Anagram windows | Find all start indices of a pattern | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Medium | All indices found; `O(n)` |
| 068 | 09-sliding-window | Window + greedy combination | Longest substring with at most k distinct | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Medium | `O(n)` window solution, no nested loops |
| 069 | 09-sliding-window | Window capstone: hard attempt | 40-minute attempt on a hard window problem | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Accepted solution, or a documented attempt naming the missing insight |

### Days 070–078 — Binary search (Phase 4 close)

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 070 | 10-binary-search | **Weekly checkpoint 10** — the template and its invariants | Implement lower/upper bound from scratch | [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Passes all 5 edge tests (empty half, single element, first/last) |
| 071 | 10-binary-search | Boundary searches | First and last occurrence of a value | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | All cases correct with one template |
| 072 | 10-binary-search | Rotated sorted arrays | Search with an unknown pivot | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | `O(log n)`; handles the pivot element |
| 073 | 10-binary-search | One-sided predicates | Find a peak using comparison hints | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Medium | `O(log n)` justified by a stated invariant |
| 074 | 10-binary-search | Binary search on the answer | Write `check(v)`, then search the value range | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Monotone predicate shown; `O(max · log)` stated |
| 075 | 10-binary-search | Harder feasibility problems | Ship packages within D days | [Capacity to Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | Correct; one-line monotonicity argument written |
| 076 | 10-binary-search | Divide and conquer on two sorted arrays | Median of two sorted inputs | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | `O(log(min(m, n)))`, or a documented attempt with the gap named |
| 077 | 10-binary-search | **Weekly checkpoint 11** | 45-minute binary-search-on-answer set, closed notes | Review: 2 problems (self-made) | Medium | 2/2 within the time box |
| 078 | 10-binary-search | **Phase 4 checkpoint** — mixed mock | 60-minute mock mixing window + binary search | Mock set (self-made) | Medium | Mock logged; revision list updated in `PROGRESS.md` |

---

## Phase 5 — Linked Lists, Stacks, and Queues (Days 079–096)

### Days 079–085 — Linked list

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 079 | 11-linked-list | Node, traversal, dummy head | Build a list from values; traverse it | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Iterative and recursive versions both correct |
| 080 | 11-linked-list | Fast/slow pointers (Floyd) | Detect a cycle; find the middle | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | `O(n)` time, `O(1)` space |
| 081 | 11-linked-list | Merging two sorted lists | Interleave with a dummy head | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Correct for empty and single-node inputs |
| 082 | 11-linked-list | Two-pass index technique | Remove the nth node from the end | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Head-removal case handled; single pass after counting |
| 083 | 11-linked-list | Reversal applications | Split at middle, reverse, merge | [Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | `O(1)` extra space; middle found correctly |
| 084 | 11-linked-list | **Weekly checkpoint 12** | 40-minute set: reverse, cycle, merge from blank files | Review set (self-made) | Medium | 3/3 rebuilt without notes |
| 085 | 11-linked-list | k-way merge with a heap | Merge k sorted lists | [Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | `O(N log k)` stated, or sequential merge with complexity noted |

### Days 086–090 — Stack

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 086 | 12-stack | Stack fundamentals; LIFO matching | Bracket matching with a stack | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | Handles nested, mismatched, and empty inputs |
| 087 | 12-stack | Monotonic stack: next greater | Implement in amortized `O(n)` | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Amortized argument written (each element pushed/popped once) |
| 088 | 12-stack | Expression evaluation | Postfix evaluation, then infix → postfix | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | Correct for negative values and integer-division semantics |
| 089 | 12-stack | Stack with auxiliary state | `O(1)` minimum tracking | [Min Stack](https://leetcode.com/problems/min-stack/) | Medium | All operations `O(1)` |
| 090 | 12-stack | **Buffer day** — Phase 5 catch-up | Re-attempt failed problems from 086–089, then attempt the hard one | [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/) | Hard | Earlier failures re-solved; hard attempt documented |

### Days 091–096 — Queue and deque (Phase 5 close)

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 091 | 13-queue-and-deque | **Weekly checkpoint 13** — queue semantics; `deque` vs list | Build a queue two ways; compare operation costs | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) | Easy | Amortized `O(1)`; explains why `list.pop(0)` is `O(n)` |
| 092 | 13-queue-and-deque | Circular buffer design | Array-based circular queue | [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) | Medium | Wrap-around, full, and empty cases all correct |
| 093 | 13-queue-and-deque | Monotonic deque | Sliding window maximum in `O(n)` | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Stale indices evicted from the front; `O(n)` proven |
| 094 | 13-queue-and-deque | Queue/stack duality | Implement a stack using queues | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) | Easy | Which operation is amortized `O(1)` is documented |
| 095 | 13-queue-and-deque | Queues for time-based events | Sliding time window with a queue | [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) | Easy | Correct counts across the full timestamp sequence |
| 096 | 13-queue-and-deque | **Mock interview #3 / Phase 5 checkpoint** | 60-minute mock: linked list + stack/queue, spoken aloud | Mock set (self-made) | Medium | Mock logged; weak areas listed for the Phase 6 warm-up |

## Phase 6 — Recursion and Backtracking (Days 097–112)

### Days 097–103 — Recursion

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 097 | 14-recursion | Recursion anatomy: base case, recursive case | Rewrite 3 loops as recursion | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | Recurrence written down; naive version stated as `O(2^n)` |
| 098 | 14-recursion | **Weekly checkpoint 14** | Timed re-solve of one Phase 5 problem + a recursion warm-up | Review set (self-made) | Medium | 1/1 within 30 minutes; recursion rewrite correct |
| 099 | 14-recursion | Memoization: stop recomputing | Add memoization to Day 097 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (memoized) | Easy | Both complexities stated: `O(2^n)` before, `O(n)` after |
| 100 | 14-recursion | Structural recursion on lists | Recursive reverse and recursive sum | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (recursive redo) | Easy | Correct base case; `O(n)` stack depth noted |
| 101 | 14-recursion | Range recursion | Recursive merge sort + recursive binary search | Self-made: recursive merge sort | Medium | Output matches `sorted()`; `O(n log n)` derived |
| 102 | 14-recursion | Log-time recursion (divide the exponent) | Fast exponentiation | [Pow(x, n)](https://leetcode.com/problems/powx-n/) | Medium | `O(log n)`; negative exponents handled |
| 103 | 14-recursion | Recursion capstone: generate structures | Generate all subsets with include/exclude | [Subsets](https://leetcode.com/problems/subsets/) | Medium | All `2^n` outputs correct; both branches explained |

### Days 104–112 — Backtracking (Phase 6 close)

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 104 | 15-backtracking | Choose → explore → un-choose | Apply the template to permutations | [Permutations](https://leetcode.com/problems/permutations/) | Medium | All `n!` outputs; undo step verified by a trace |
| 105 | 15-backtracking | **Weekly checkpoint 15** — combinations and pruning | Combination sum with element reuse | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | No duplicate combinations; pruning justified |
| 106 | 15-backtracking | Mapping + backtracking | Phone keypad letter combinations | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | Empty input handled |
| 107 | 15-backtracking | Duplicate-aware enumeration | Skip equal siblings while branching | [Permutations II](https://leetcode.com/problems/permutations-ii/) | Medium | Duplicates eliminated without a global result set |
| 108 | 15-backtracking | Constraint propagation | Place queens, prune conflicts | [N-Queens](https://leetcode.com/problems/n-queens/) | Hard | All solutions found; pruning rule stated |
| 109 | 15-backtracking | Backtracking on a mutable board | Solve Sudoku with undo | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | Hard | Solves the given board; board restored after failed branches |
| 110 | 15-backtracking | DFS with undo on a grid | Mark, recurse, restore | [Word Search](https://leetcode.com/problems/word-search/) | Medium | Board state restored after every failed branch |
| 111 | 15-backtracking | Backtracking capstone | Unseen medium in a 35-minute box | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Medium | Solved within the box; complexity stated |
| 112 | 15-backtracking | **Weekly checkpoint 16 / Phase 6 checkpoint** | Re-derive all 5 templates from memory, timed | Self-made template drill | Medium | All 5 written from a blank file; gaps logged in `PROGRESS.md` |

---

## Phase 7 — Trees, BSTs, Heaps, and Priority Queues (Days 113–131)

### Days 113–121 — Binary trees

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 113 | 16-trees | Node, building trees, the three DFS orders | Pre/in/post-order, recursive | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Easy | All three orders correct on an unbalanced tree |
| 114 | 16-trees | Iterative traversal with an explicit stack | Convert one traversal to iterative | Self-made: iterative vs recursive preorder | Medium | Iterative output matches recursive exactly |
| 115 | 16-trees | BFS level order | Level-by-level queue processing | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | Levels returned as separate lists |
| 116 | 16-trees | Depth and height recursion | Max depth, then min depth | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | Post-order combine correct; skewed tree handled |
| 117 | 16-trees | Root-to-leaf path accumulation | Accumulate values along the path | [Path Sum](https://leetcode.com/problems/path-sum/) | Easy | Negatives handled; partial paths don't count |
| 118 | 16-trees | Aggregation in one DFS | Diameter in a single traversal | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | One traversal only; `O(n)` stated |
| 119 | 16-trees | **Weekly checkpoint 17** | 45-minute set: 3 tree problems from memory | Review set (self-made) | Medium | 3/3 without notes |
| 120 | 16-trees | Construct from traversals | Rebuild a tree from preorder + inorder | [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | Correct tree; `O(n)` with an index map stated |
| 121 | 16-trees | **Buffer day** — tree catch-up | Re-attempt failures from 113–120, then LCA | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | Failures re-solved; LCA correct for non-BST shapes |

### Days 122–126 — Binary search trees

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 122 | 17-binary-search-tree | The BST invariant; search and insert | Walk the tree using the ordering rule | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | Easy | Uses the invariant — never a full traversal |
| 123 | 17-binary-search-tree | Validation with `(low, high)` bounds | Detect violations anywhere in the tree | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | Catches right-subtree and equal-value violations |
| 124 | 17-binary-search-tree | In-order streaming | k-th smallest without building a list | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Medium | `O(h + k)`; correct when `k = n` |
| 125 | 17-binary-search-tree | Deletion: 0, 1, 2 children | Implement all three cases | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) | Medium | All cases correct; invariant preserved afterward |
| 126 | 17-binary-search-tree | **Weekly checkpoint 18** | 40-minute BST mock: validate + k-th smallest | Review set (self-made) | Medium | Both correct within the time box |

### Days 127–131 — Heaps and priority queues (Phase 7 close)

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 127 | 18-heaps-and-priority-queue | Heap mechanics: sift up/down, `heapq` | Trace by hand, then code top-k | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Size-k heap; `O(n log k)` stated |
| 128 | 18-heaps-and-priority-queue | Top-k patterns | Counter + heap, plus a sort fallback | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Two working approaches; complexities compared |
| 129 | 18-heaps-and-priority-queue | Heap-based scheduling | Order tasks to minimize idle time | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | Formula and/or heap solution justified |
| 130 | 18-heaps-and-priority-queue | Two heaps for a running median | Maintain a median stream | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | `O(log n)` add, `O(1)` find; balanced halves argued |
| 131 | 18-heaps-and-priority-queue | **Mock interview #4 / Phase 7 checkpoint** | 60-minute mock: tree + heap, spoken aloud | Mock set (self-made) | Medium | Mock logged; revision topics listed |

---

## Phase 8 — Graphs and Graph Algorithms (Days 132–150)

### Days 132–145 — Graphs

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 132 | 19-graphs | Representations: adjacency list vs matrix | Build both from an edge list; count degrees | Self-made: representation drill | Easy | Both representations agree on every degree |
| 133 | 19-graphs | **Weekly checkpoint 19** — BFS fundamentals | BFS with visited-on-enqueue; level distances | Self-made: BFS distance drill | Medium | Distances correct; `O(V + E)` stated |
| 134 | 19-graphs | DFS recursive and iterative | Count connected components | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | All islands found; `O(mn)` stated |
| 135 | 19-graphs | Grid as a graph; multi-source BFS | Push all sources into the queue at once | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | Minutes correct; impossible case returns −1 |
| 136 | 19-graphs | Cycle detection in a directed graph | Three-color (white/gray/black) state machine | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Cycles detected including self-loops |
| 137 | 19-graphs | Topological sort with Kahn's algorithm | In-degree queue ordering | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | Valid order produced, or `[]` on a cycle |
| 138 | 19-graphs | Components on a grid | Flood fill with area tracking | [Max Area of Island](https://leetcode.com/problems/max-area-of-island/) | Medium | Rotated shapes handled; `O(mn)` stated |
| 139 | 19-graphs | Bipartiteness by two-coloring | BFS coloring check | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | Medium | Odd cycles detected correctly |
| 140 | 19-graphs | **Weekly checkpoint 20** | 45-minute set: BFS + topological sort | Review set (self-made) | Medium | 2/2 within the time box |
| 141 | 19-graphs | Dijkstra with a heap | Weighted single-source shortest path | [Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | `O(E log V)`; stale heap entries skipped |
| 142 | 19-graphs | Bounded relaxation; why Dijkstra fails | Relax with a hop limit | [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Medium | Correct with the `k`-relaxation constraint |
| 143 | 19-graphs | Hierarchical edge ordering | Cover all edges of a multigraph | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/) | Hard | Lexicographic ordering correct |
| 144 | 19-graphs | Grid shortest paths | Multi-source BFS on a grid | [01 Matrix](https://leetcode.com/problems/01-matrix/) | Medium | Distances to the nearest zero correct |
| 145 | 19-graphs | **Buffer day** — graph catch-up | Re-attempt failures from 132–144, then an unseen problem | [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | Failures re-solved; unseen problem attempted and documented |

### Days 146–150 — Union find (Phase 8 close)

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 146 | 23-union-find | DSU from scratch: find, union, rank | Path compression + union by rank | [Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | Medium | Component count correct; `α(n)` explained |
| 147 | 23-union-find | **Weekly checkpoint 21** — DSU applications | Find the edge that creates a cycle | [Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | Cycle edge identified; union order respected |
| 148 | 23-union-find | Union by key; grouping members | Merge accounts sharing an identity | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | Medium | Groups correct; keys normalized |
| 149 | 23-union-find | Kruskal's MST (greedy + DSU) | Sort edges, accept joins, sum weights | [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | MST cost correct; `O(E log E)` stated |
| 150 | 23-union-find | **Mock interview #5 / Phase 8 checkpoint** | 60-minute mock: graph + DSU, spoken aloud | Mock set (self-made) | Medium | Mock logged in `PROGRESS.md` |

## Phase 9 — Greedy Algorithms and Dynamic Programming (Days 151–168)

### Days 151–155 — Greedy

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 151 | 20-greedy | Greedy choice property; exchange arguments | Write the proof *before* writing the code | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Easy | Proof recorded in the docstring; output correct |
| 152 | 20-greedy | Reachability greedy | Forward reachability scan | [Jump Game](https://leetcode.com/problems/jump-game/) | Medium | `O(n)`; reachability argument written |
| 153 | 20-greedy | Greedy with accumulation | Farthest-reach jumping | [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium | Minimum jumps; `O(n)` |
| 154 | 20-greedy | **Weekly checkpoint 22** — greedy vs DP | Classify 5 statements: greedy or DP? | Self-made classification drill | Medium | ≥ 4/5 correct **with written reasons** |
| 155 | 20-greedy | Interval/scheduling greedy | Sort by end, count what must be removed | [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Optimality sketch written; correct count |

### Days 156–168 — Dynamic programming (Phase 9 close)

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 156 | 21-dynamic-programming | DP mindset: state → transition → base case | Convert a memoized recursion into a table | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (tabulation redo) | Easy | Table built; `O(n)` time and space stated |
| 157 | 21-dynamic-programming | Linear DP with an adjacency constraint | House-robber recurrence | [House Robber](https://leetcode.com/problems/house-robber/) | Medium | Correct for `n = 1` and `n = 2` |
| 158 | 21-dynamic-programming | Grid DP | Paths around obstacles | [Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | 2-D table correct; space reduction noted |
| 159 | 21-dynamic-programming | Minimum-cost path | Bottom-up over a triangle | [Triangle](https://leetcode.com/problems/triangle/) | Medium | Correct bottom-up indexing |
| 160 | 21-dynamic-programming | Knapsack 0/1 | Backward capacity loop + reconstruction | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | `O(n · cap)`; the subset itself can be reconstructed |
| 161 | 21-dynamic-programming | **Weekly checkpoint 23** — recurrence drills | Write only state + transition, 25 min, 3 problems | Self-made recurrence drill | Medium | 3/3 transitions correct |
| 162 | 21-dynamic-programming | Unbounded knapsack | Minimum coins and coin-count variants | [Coin Change](https://leetcode.com/problems/coin-change/) | Medium | Impossible case returns −1; `O(n · amount)` |
| 163 | 21-dynamic-programming | String 2-D DP | LCS with two-row space optimization | [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | Two-row version matches the full table |
| 164 | 21-dynamic-programming | Edit distance | Insert/delete/replace recurrence | [Edit Distance](https://leetcode.com/problems/edit-distance/) | Hard | `O(n·m)`; boundary row/column correct |
| 165 | 21-dynamic-programming | Decision DP over prefixes | Segment a string into dictionary words | [Word Break](https://leetcode.com/problems/word-break/) | Medium | Prefix segmentation correct; re-check loop `O(n²)` |
| 166 | 21-dynamic-programming | Subsequence DP over arrays | LIS in `O(n²)`, then `O(n log n)` | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | Both versions work; both complexities stated |
| 167 | 21-dynamic-programming | State beyond a single index | Two-state DP with a cooldown-style constraint | [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium | Every state and transition named explicitly |
| 168 | 21-dynamic-programming | **Weekly checkpoint 24 / Mock interview #6 / Phase 9 checkpoint** | 75-minute mock, then write the DP state sheet from memory | Mock + self-made audit | Hard | Mock logged; state sheet lists ≥ 10 states with transitions |

---

## Phase 10 — Advanced Topics, Mixed Practice, and Interview Revision (Days 169–180)

### Days 169–171 — Trie

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 169 | 22-trie | Node design; insert, search, prefix | Implement the trie from scratch | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | All three operations pass their tests |
| 170 | 22-trie | Prefix counts; typeahead | Suggest words for each typed prefix | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Medium | Suggestions correct and lexicographically sorted |
| 171 | 22-trie | Trie + backtracking on a grid | Prune the search with the trie | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | All dictionary words found; pruning demonstrated |

### Days 172–173 — Bit manipulation

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 172 | 24-bit-manipulation | AND/OR/XOR and shifts | Micro-drills: get, set, clear, toggle a bit | [Single Number](https://leetcode.com/problems/single-number/) | Easy | XOR solution in `O(1)` extra space |
| 173 | 24-bit-manipulation | Subset masks; bit counting | Enumerate all `2^n` subsets with masks; count 1-bits | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | `x & (x - 1)` used; subset enumeration verified |

### Days 174–175 — Intervals

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 174 | 25-intervals | Merge and sweep | Re-derive interval merging from a blank file | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Correct; the touching-interval rule stated explicitly |
| 175 | 25-intervals | **Weekly checkpoint 25** — insertion and sweep line | Insert an interval; sweep-line overlap counting | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | Three-region split correct; sweep-line drill done |

### Days 176–177 — Advanced algorithms

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 176 | 26-advanced-algorithms | All-pairs shortest paths; negative weights (overview) | Set up Floyd–Warshall on a small graph | [Find the City with the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/) | Medium | `O(V³)` table correct for the sample input |
| 177 | 26-advanced-algorithms | **Buffer day** — advanced-topics overview | Implement rolling-hash substring search; diff against naive | Self-made: Rabin–Karp vs naive | Hard | Matches naive on randomized tests; collision risk stated |

### Days 178–180 — Patterns and revision (final)

| Day | Topic | Concept / objective | Practice task | Suggested problem | Difficulty | Completion criterion |
|---|---|---|---|---|---|---|
| 178 | 27-patterns-and-revision | Pattern identification under time pressure | Read 8 problem statements; name pattern + expected complexity, **no code** | Self-made identification drill | Medium | ≥ 7/8 correct in under 15 minutes |
| 179 | 27-patterns-and-revision | Timed mixed set + weak-topic re-solve | 60-minute set of 3 mediums; re-solve your 2 weakest problems overall | Self-made set | Medium | 3 attempted honestly; both re-solves clean, no notes |
| 180 | 27-patterns-and-revision | **Final mock interview + 180-day retrospective** | 90-minute mock; write the retrospective; plan the next cycle | Final mock (self-made) | Hard | Mock completed; `PROGRESS.md` counters finalized honestly |

---

## Appendix A — Weekly checkpoints

Every 7th day is a timed, closed-notes re-solve of that week's material. Log
the result (pass/gap) in `PROGRESS.md`.

| # | Day | Closes out |
|---|---|---|
| 1 | 007 | Python basics |
| 2 | 014 | Complexity analysis |
| 3 | 021 | Arrays (part 1) |
| 4 | 028 | Strings |
| 5 | 035 | Sorting intro |
| 6 | 042 | Hashing |
| 7 | 049 | Hashing + two pointers |
| 8 | 056 | Two pointers + prefix sums |
| 9 | 063 | Prefix sums + sliding window |
| 10 | 070 | Binary search template |
| 11 | 077 | Binary search on answer |
| 12 | 084 | Linked lists |
| 13 | 091 | Stacks + queues |
| 14 | 098 | Recursion intro |
| 15 | 105 | Backtracking templates |
| 16 | 112 | Phase 6 — full template recall |
| 17 | 119 | Tree traversals |
| 18 | 126 | BST |
| 19 | 133 | Graph representations + BFS |
| 20 | 140 | DFS + topological sort |
| 21 | 147 | Union-find |
| 22 | 154 | Greedy vs DP classification |
| 23 | 161 | DP recurrences |
| 24 | 168 | Phase 9 — DP state sheet |
| 25 | 175 | Intervals |
| 26 | — | Days 176–180 run the final mock and retrospective instead |

## Appendix B — Mock interviews and buffer days

| Type | Days | Format |
|---|---|---|
| Mock #1 | 040 | 60 min, 3 problems across Phase 2 |
| Mock #2 | 060 | 50 min, 1 medium + 1 review problem, spoken aloud |
| Mock #3 | 096 | 60 min, linked list + stack/queue |
| Mock #4 | 131 | 60 min, tree + heap |
| Mock #5 | 150 | 60 min, graph + DSU |
| Mock #6 | 168 | 75 min, DP-heavy |
| Final mock | 180 | 90 min, anything from the roadmap |
| Buffer days | 015, 046, 090, 121, 145, 177 | Catch up on the phase just finished; nothing new is introduced |

A mock session = read the statement aloud, state the approach and its
complexity **before** coding, implement, run your own test cases, then note
what you would do differently. Record it in `PROGRESS.md`.

## Appendix C — Revision strategy

1. **Spaced re-solves** — after first solving a problem, re-solve it on
   Day + 1, Day + 7, and Day + 30 (put the dates in the docstring's
   *Review Date* field).
2. **Weekly checkpoints** — Appendix A is the scheduled version of (1).
3. **Topic revision** — anything you could not re-derive goes into the
   *Topics requiring revision* table in `PROGRESS.md` with a next-review date.
4. **Phase checkpoints** — the last day of each phase consolidates it before
   the next phase's prerequisites begin.
5. **Days 178–180** — pattern-only revision: no new topics, retrieval and
   communication practice.

## Appendix D — After Day 180

Do not stop — loop the weak areas: pull every topic still unchecked in
`PROGRESS.md`, run one mock per week, and keep adding new problems only where
the pattern is still shaky. The repository structure supports this indefinitely:
topic folders and the problem template are unchanged.
