# Merge Intervals

| Field | Value |
|---|---|
| Day | `day-06` |
| Track | `dsa` |
| Topic | `05-sorting` — see `resources/topics/` |
| Difficulty | Medium |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/merge-intervals/ |

## Problem summary

Given a list of intervals `[start, end]`, merge every pair that overlaps **or
merely touches** and return the resulting cover in ascending order. `[1, 3]`
and `[2, 6]` become `[1, 6]`; `[1, 4]` and `[4, 5]` also become `[1, 5]`,
because the union has no gap. The output must be disjoint and strictly
separated, so the answer is the minimal set of intervals whose union is
unchanged.

### Input

- `intervals: list[list[int]]` — `0 <= len(intervals) <= 10⁴`; each element is
  exactly two integers `[start, end]` with `start <= end`, and
  `-10⁴ <= start, end <= 10⁴`.
- The list is **not** guaranteed to be sorted by start, and intervals may be
  nested, duplicated, or share an endpoint.
- Anything that is not a `[start, end]` pair with `start <= end` is malformed
  input and raises `ValueError` here (LeetCode guarantees valid input; this
  repository's functions stay total).

### Output

- `list[list[int]]` — the merged intervals, sorted by start, pairwise disjoint,
  with `previous_end < next_start` (strict, so touching was already merged).

## Approach

1. **Validate** every element: it must hold exactly two integers and satisfy
   `start <= end`, otherwise raise `ValueError`.
2. **Sort by start** using `sorted(...)`, which returns a new list — the caller's
   list is never reordered.
3. **Scan once**, keeping the group currently being built as
   `current_start, current_end`:
   - if `start <= current_end`, the interval overlaps or touches the group, so
     extend it with `current_end = max(current_end, end)` — `max` is what keeps
     a nested interval like `[2, 3]` from shrinking `[1, 10]`;
   - otherwise the group is closed: append it and start a new group at this
     interval.
4. Append the final group and return.

## Why this approach works

After sorting by start, consider the group under construction and the next
interval. Its start is at least the group's start. It merges with the group
exactly when `start <= current_end`; when `start > current_end` there is an
open gap `(current_end, start)`, and every *later* interval starts at or after
`start`, so none of them can reach back across that gap either. That is the
invariant: **a group is finished as soon as one interval starts beyond its
end**. It proves both halves of the requirement — no merge is missed, and no
two returned intervals touch or overlap, so the output is minimal. Using `<=`
rather than `<` is what makes touching intervals (`[1, 4]`, `[4, 5]`) merge;
using `max` on the ends is what handles nesting.

## Complexity

- **Time:** O(n log n) — the sort dominates; the merge scan is a single pass
  with O(1) work per interval.
- **Space:** O(n) auxiliary — the sorted copy plus a group per disjoint result
  (the returned list itself holds at most `n` intervals).

## Edge cases

- Empty input `[]` → `[]`: return before touching `sorted(...)[0]`.
- A single interval `[[5, 7]]` → `[[5, 7]]`: the scan never merges and appends
  the seeded group at the end.
- Ordering: `[[8, 10], [1, 3], [2, 6], [15, 18]]` → `[[1, 6], [8, 10], [15, 18]]`
  — the sort is what makes the scan valid.
- Touching: `[[1, 4], [4, 5]]` → `[[1, 5]]`; chains like
  `[[1, 2], [2, 3], [3, 4]]` → `[[1, 4]]`.
- Nested: `[[1, 10], [2, 3], [4, 8]]` → `[[1, 10]]` — only `max` prevents the
  inner ends from shrinking the group.
- Disjoint but interleaved ends: `[[1, 2], [3, 4]]` stays two intervals.
- Duplicates: `[[1, 2], [1, 2]]` → `[[1, 2]]`.
- Negative coordinates, including an interval crossing zero:
  `[[-5, -1], [-2, 3], [10, 12]]` → `[[-5, 3], [10, 12]]`.
- Zero-length interval `[[4, 4]]` → `[[4, 4]]`; `[[4, 4], [4, 6]]` → `[[4, 6]]`.
- Malformed input: `[[]]`, `[[1]]`, `[[3, 1]]`, `[[1, 2, 3]]` → `ValueError`.
- Maximum size: `10⁴` intervals that all overlap collapse to one in O(n log n)
  time and O(n) space.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[[1, 3], [2, 6], [8, 10], [15, 18]]` | `[[1, 6], [8, 10], [15, 18]]` | the statement's example |
| `[[1, 4], [4, 5]]` | `[[1, 5]]` | touching intervals merge |
| `[[1, 4], [0, 4]]` | `[[0, 4]]` | same end, different start |
| `[[1, 4], [2, 3]]` | `[[1, 4]]` | nesting must not shrink the group |
| `[[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]` | `[[1, 10]]` | one interval swallows the rest |
| `[[1, 2], [3, 4]]` | `[[1, 2], [3, 4]]` | a real gap stays a gap |
| `[]` | `[]` | nothing to merge |
| `[[5, 7]]` | `[[5, 7]]` | single interval |
| `[[1, 2], [1, 2]]` | `[[1, 2]]` | duplicates |
| `[[-5, -1], [-2, 3], [10, 12]]` | `[[-5, 3], [10, 12]]` | negatives, crossing zero |
| `[[4, 4]]`, `[[4, 4], [4, 6]]` | `[[4, 4]]`, `[[4, 6]]` | zero-length interval |
| `[[]]`, `[[1]]`, `[[3, 1]]`, `[[1, 2, 3]]` | raises `ValueError` | malformed input |
| 500 random interval lists over `-20…20` | equals a fixed-point pairwise-merge reference | differential check, different algorithm |
| the same 500 lists | merged output covers exactly the same integer points as the input | no point lost or invented |
| `10⁴` overlapping intervals | `[[0, 10⁴]]` | maximum-size collapse |

## What I learned

- **Pattern:** "sort by start, then scan" is the interval reflex — the sort
  turns an arbitrary set into a sequence where the merge condition is local.
- **Pitfall:** `start < current_end` silently leaves touching intervals split;
  the problem's union semantics requires `start <= current_end`, and the end has
  to be a `max`, not an overwrite.
- **Differently next time:** test against a reference that merges pairs to a
  fixed point. It is a different algorithm, so the differential test catches the
  sort/scan reasoning errors a hand-written expected list would hide.

**Review date:** 2026-11-09 (1 day) · 2026-11-15 (7 days) · 2026-12-08 (30 days)
