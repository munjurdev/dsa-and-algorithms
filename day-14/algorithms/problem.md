# Weekly Checkpoint 02 — Three Closed-Notes Re-solves + the `list.pop(0)` Cost Drill

| Field | Value |
|---|---|
| Day | `day-14` |
| Track | `algorithms` |
| Topic | `12-stack` (checkpoint behind Days 08–13) — see `resources/topics/` |
| Difficulty | Medium |
| Platform | LeetCode (re-solves) + self-made drill |
| URL | https://leetcode.com/problems/container-with-most-water/ · https://leetcode.com/problems/find-all-anagrams-in-a-string/ · https://leetcode.com/problems/search-in-rotated-sorted-array/ |

## Problem summary

Checkpoint 02 is not a new problem — it is a **timed, closed-notes rebuild**
of one problem per pattern family from Days 08–13, followed by a cost
question about Python lists. The completion criterion from `ROADMAP.md` is
3/3 rebuilt from blank files, with each solution's cost stated, plus an
explanation of why `list.pop(0)` is O(n).

The three re-solves, chosen to span the phase rather than repeat one family:

| # | Problem | From | Pattern | Target complexity |
|---|---|---|---|---|
| 1 | Container With Most Water | Day 08 | converging two pointers | O(n) time, O(1) space |
| 2 | Find All Anagrams in a String | Day 11 | fixed-width sliding window | O(n) time, O(m) space |
| 3 | Search in Rotated Sorted Array | Day 12 | binary search with a sorted-half test | O(log n) time, O(1) space |

Day 09's prefix-sum pair, Day 10's variable window, and Day 13's linked-list
pair were not re-solved today; they stay on their own spaced-review dates
(recorded in their `problem.md` files).

## Approach

**1. Container With Most Water.** Start with the widest pair (`left = 0`,
`right = n - 1`) and move the **shorter** side inward each step. Width can only
decrease, so the shorter line cannot be part of any future better rectangle:
any pair using it has less width and height at most its own.

**2. Find All Anagrams in a String.** Slide a window of length `len(p)` over
`s`. Maintain a `Counter` for the window and one for `p`; when the two dicts
are equal, the window is an anagram. Each step removes one character and adds
one, so the counters are updated in O(1) average and never rebuilt — the
"re-count the window each time" version is O(n·m) and is exactly what the
window is for.

**3. Search in Rotated Sorted Array.** At every midpoint, at least one half is
sorted: compare `nums[low] <= nums[mid]` to identify it. If the target lies
within the sorted half's bounds, search there; otherwise the target must be in
the other half. The discarded half never needs another look, so the range
halves as usual.

**4. Why `list.pop(0)` is O(n).** A Python `list` is a contiguous array of
pointers: index 0 is at a fixed offset from the start of the buffer. Removing
the first element requires shifting every remaining element one slot toward
the front (a `memmove` of `n - 1` pointers) and decrementing the length, so
the cost is proportional to the number of elements left, not constant. A queue
that dequeues `n` items with `pop(0)` therefore pays `n + (n-1) + ... + 1`,
i.e. **O(n²)** total, even though every individual call looks cheap in the
source. `collections.deque` stores elements in fixed-size blocks plus a head
index; `popleft()` advances the head and only occasionally frees a block, so it
is O(1) amortized. Use `deque` (or an index pointer over the list, when items
are never inserted) for queues.

## Why this approach works

**Invariant, container:** the current pair is the best among all pairs whose
outer boundary has not been passed; discarding the shorter side is safe
because every pair containing it is no better than the current one — the
argument is a discard proof, not a heuristic.

**Invariant, anagrams:** at the top of each step the window covers
`s[start : start + m]` and the two counters describe exactly those characters,
so equality means "multiset equal", which is the definition of an anagram.
No window is skipped, so every start index is considered exactly once.

**Invariant, rotated search:** the target, if present, always lies inside
`[low, high]`; the sorted-half test identifies which sub-range can contain it,
and the bounds check moves the boundary so that only candidates survive. The
strict inequality on the target side (`target < nums[mid]` / `target <= nums[high]`) is
what keeps the half containing the already-checked midpoint from being
re-included forever.

**Why the cost drill is a real check, not trivia:** the measured totals below
grow ~4× per doubling of `n`, which is the observable signature of O(n²); a
constant-time dequeue would grow ~2×. The numbers are printed by the solution
so the claim is evidence-backed rather than asserted.

## Complexity

- **Container With Most Water:** O(n) time — each step moves one pointer
  inward, so at most `n - 1` steps; O(1) space.
- **Find All Anagrams:** O(n + m) time — build the pattern counter once, then
  one removal and one insertion per start index; dict-equality of two counters
  over a fixed alphabet is O(1) here and O(Σ) in general. O(m + Σ) space.
- **Search in Rotated Sorted Array:** O(log n) time — the range halves every
  iteration and each iteration does constant work; O(1) space.
- **Queue on `list.pop(0)`:** O(n) per dequeue, O(n²) for `n` dequeues, versus
  O(1) amortized per `popleft()` and O(n) total for a `deque`.

Measured (`python solution.py`, 2026-11-19, CPython on this machine):

| n | `list.pop(0)` total | `deque.popleft()` total |
|---|---|---|
| 2,000 | 0.246 ms | 0.082 ms |
| 4,000 | 0.937 ms | 0.146 ms |
| 8,000 | 4.974 ms | 0.289 ms |

## Edge cases

- **Container:** empty list and single line → `0` (no pair); two lines → the
  shorter height; equal heights on both ends → move either side; zeros → area
  0; maximum-length input still one pass.
- **Anagrams:** pattern longer than the text → `[]`; empty text → `[]`; single
  character pattern → every matching index; overlapping matches (`"abab"`,
  `"ab"` → `[0, 1, 2]`) — the window must step by one, not by `len(p)`;
  repeated letters in the pattern (multiset, not set).
- **Rotated search:** empty array → `-1`; single element; target below the
  minimum or above the maximum → `-1`; rotation of 0 (not rotated at all);
  rotation of `n - 1` (two-element wraparound, `[3, 1]`); target at the pivot
  or at either end.
- **Cost drill:** an empty list must not be popped; timing is reported, never
  asserted, because wall-clock numbers are machine-dependent and would make
  the test suite flaky.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[1,8,6,2,5,4,8,3,7]` | `49` | statement example for the container |
| `[]`, `[5]` | `0` | fewer than two lines → no container |
| `[1,1]` | `1` | minimum real container |
| `[4,3,2,1,4]` | `16` | best pair is the two ends |
| `[1,2,1]` | `2` | ties and a non-monotone middle |
| 300 random height lists (size 0–40) | brute-force max over all pairs | randomized differential check |
| `"cbaebabacd"`, `"abc"` | `[0, 6]` | statement example for anagrams |
| `"abab"`, `"ab"` | `[0, 1, 2]` | overlapping matches |
| `""`/`"a"`, `"a"`/`"ab"` | `[]` | empty text; pattern longer than text |
| `"aa"`, `"aa"` | `[0]` | repeated letters, duplicates in the pattern |
| `"abc"`, `"d"` | `[]` | no match |
| 300 random texts over `abc` | sorted-window brute force | randomized differential check |
| `[4,5,6,7,0,1,2]`, target 0 / 3 | `4` / `-1` | statement examples, found and absent |
| `[]`, target 5 | `-1` | empty array |
| every rotation of every size 0–7 sorted array, targets −22..22 | index in that rotation or `-1` | exhaustive rotation check, not just the example rotation |
| `n = 2,000 / 4,000 / 8,000` queue drains | measured, printed | shows quadratic vs linear growth |

## What I learned

- **Pattern:** the three families reduce to three different discard proofs —
  discard the shorter line, discard windows that leave the fixed width, discard
  the half that cannot contain the target. Being able to name *what is
  discarded and why* is what made the rebuilds mechanical instead of
  memory-based.- **Pitfall:** the anagram window has two failure modes the statement example
  cannot expose: stepping by `len(p)` loses overlapping matches, and rebuilding
  a Counter per window quietly turns O(n) into O(n·m). The brute-force
  differential test catches both.
- **Differently next time:** answer structural cost questions (like `pop(0)`)
  with a measurement *and* the mechanism ("shifts `n-1` pointers"), because
  either one alone can be wrong — the mechanism without data invites
  hand-waving, and the data without the mechanism does not generalize to
  `insert(0, x)`, `del list[0]`, or slicing.

**Review date:** 2026-11-20 (1 day) · 2026-11-26 (7 days) · 2026-12-19 (30 days)
