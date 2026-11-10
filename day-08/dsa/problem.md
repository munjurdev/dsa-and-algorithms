# 3Sum

| Field | Value |
|---|---|
| Day | `day-08` |
| Track | `dsa` |
| Topic | `07-two-pointers` — see `resources/topics/` |
| Difficulty | Medium |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/3sum/ |

## Problem summary

Given an integer array `nums`, find every **unique** triplet of elements at
**three distinct indices** whose values add up to zero. The answer must not
contain duplicate triplets, even when the same value appears many times in the
input. The natural `O(n²)` pair search hides a trap: skipping duplicates
correctly is what separates an accepted solution from a correct-looking one.

### Input

- `nums: list[int]` — `0 <= len(nums) <= 3000` on the platform, each value
  `-10⁵ <= nums[i] <= 10⁵`, unsorted, duplicates allowed.
- This implementation is total: every list, including the empty one, returns a
  list rather than raising.

### Output

- `list[list[int]]` — each triplet in ascending order, the list of triplets
  sorted ascending. No triplet appears twice, and no triplet reuses an index
  (which only matters when duplicates exist in the input).

## Approach

1. **Sort** a copy of `nums`; the pointer movement below depends on order.
2. Walk a fixed position `fixed` from `0` to `n - 3`, treating `nums[fixed]` as
   the first element of the triplet.
   - If `nums[fixed] > 0`, break: the array is sorted, so every remaining value
     is positive and the sum cannot reach zero.
   - If `nums[fixed]` equals the previous fixed value, skip it — the same
     triplets would be rebuilt.
3. Set `left = fixed + 1` and `right = n - 1`, then converge:
   - `total < 0` → `left += 1` (the only way to raise the sum);
   - `total > 0` → `right -= 1` (the only way to lower it);
   - `total == 0` → record the triplet, advance both pointers, then skip every
     duplicate value on each side.
4. Return the recorded triplets.

No set of tuples is needed: duplicates are prevented **before** they are
created, at both the fixed position and the pointer positions.

## Why this approach works

**Sorted order makes pointer movement sound.** For a fixed `value`, with
`left < right`, the pair sum `ordered[left] + ordered[right]` is the only sum
reachable from both ends. If it is below `-value`, then for this `left`, every
`right' <= right` gives a smaller sum — none can work — so `left` may advance
without losing an answer. Symmetrically, a sum above `-value` rules out the
whole column for this `right`. Each step discards only impossible pairs, so the
scan is complete.

**The skip rules emit each triplet exactly once.** After sorting, a triplet has
one canonical ascending form, and the smallest element is the one chosen as
`fixed`. Skipping a repeated fixed value removes every alternate index that
could form the same first element. After a match, all remaining positions
holding the same `left` value pair with the same `right` value to give the same
triplet, and likewise for repeated `right` values — hence both skip loops.
Together these make the output duplicate-free without post-filtering.

**The early break is exact.** With `nums[fixed] > 0`, all later elements are at
least that large and positive, so any triplet using them sums to more than
zero. Stopping there loses nothing.

## Complexity

- **Time:** O(n²) — sorting is O(n log n); the outer loop runs at most `n`
  times and each two-pointer scan advances a pointer at most `n` steps, so the
  scans total O(n²). The duplicate-skip loops only consume positions the scans
  would have visited anyway.
- **Space:** O(1) auxiliary beyond the output — the sorted copy is O(n) and is
  required because the caller's list must not be mutated; no hash set of
  results is used.

## Edge cases

- Empty list, one element, or two elements → `[]`.
- All positive → `[]` via the early break; all negative → `[]` after the full
  scan finds no `right` side to lift the sum.
- `[0, 0, 0]` → `[[0, 0, 0]]`; `[0, 0, 0, 0]` → the same single triplet, not
  three index combinations.
- Duplicate fixed values: `[-1, -1, -1, 2, 2, 2]` → `[[-1, -1, 2]]`, not nine
  index triples.
- Duplicate partner values around a match: `[-2, 0, 1, 1, 2]` →
  `[[-2, 0, 2], [-2, 1, 1]]`; the two `1`s are a legitimate triplet because
  they are distinct indices.
- Triplets containing repeated values: `[-2, 0, 0, 2, 2]` → `[[-2, 0, 2]]`.
- Fewer than three elements is handled by loop bounds, not a special case.
- Input is not mutated: sorting happens on a copy.
- Largest values `±10⁵` summed three times stay exact in Python ints, so no
  overflow path exists.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[-1, 0, 1, 2, -1, -4]` | `[[-1, -1, 2], [-1, 0, 1]]` | the statement's example |
| `[]`, `[0]`, `[1, 2]` | `[]` | fewer than three elements |
| `[1, 2, 3]` | `[]` | all positive, early break |
| `[-3, -2, -1]` | `[]` | all negative |
| `[0, 0, 0, 0]` | `[[0, 0, 0]]` | duplicates collapse to one triplet |
| `[-1, 0, 1, 0]` | `[[-1, 0, 1]]` | two zeros, one triplet |
| `[-2, 0, 1, 1, 2]` | `[[-2, 0, 2], [-2, 1, 1]]` | repeated partner value is two indices |
| `[-1, -1, -1, 2, 2, 2]` | `[[-1, -1, 2]]` | duplicate fixed and partner values |
| `[-5, 2, 3, 0]` | `[[-5, 2, 3]]` | negatives with a zero neighbour |
| `[3, -1, -1, 2, -4]` | `[[-1, -1, 2]]` | caller's list untouched |
| every array of length 0–6 over `-3…3` | equals an `itertools.combinations` oracle | exhaustive differential check |
| 300 random arrays of length 0–30 over `-8…8` | equals the oracle | randomized duplicates check |

## What I learned

- **Pattern:** sort once, then reuse a *linear* two-pointer scan for every
  fixed position — the O(n²) comes from `n` fixed positions, not from a nested
  pair loop.
- **Pitfall:** duplicates are a correctness problem in three separate places
  (fixed value, left value after a match, right value after a match). Fixing
  only the fixed-value skip still returns repeated triplets such as
  `[-2, 1, 1]` from `[-2, 1, 1, 1]`.
- **Differently next time:** write the brute-force oracle first. It settled the
  exact output order and every duplicate question in one line, so the fast
  version had something to disagree with instead of my memory.

**Review date:** 2026-11-11 (1 day) · 2026-11-17 (7 days) · 2026-12-10 (30 days)
