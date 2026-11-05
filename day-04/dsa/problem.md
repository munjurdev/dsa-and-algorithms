# Two Sum

| Field | Value |
|---|---|
| Day | `day-04` |
| Track | `dsa` |
| Topic | `02-arrays` — see `resources/topics/` |
| Difficulty | Easy |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/two-sum/ |

## Problem summary

Given an unsorted array of integers `nums` and an integer `target`, find the
two **distinct indices** `i` and `j` such that `nums[i] + nums[j] == target`.
Exactly one such pair exists when the input is valid. The answer is the pair
of indices, not the values — so a duplicate value at two positions is a
legitimate answer, while the same position used twice is not.

### Input

- `nums: list[int]` — `2 <= len(nums) <= 10⁴`, `-10⁹ <= nums[i] <= 10⁹`,
  unsorted, duplicates allowed.
- `target: int` — `-10⁹ <= target <= 10⁹`.
- Guaranteed: exactly one valid index pair.

### Output

- `list[int]` — `[i, j]` with `i < j` and `nums[i] + nums[j] == target`,
  in either order as far as LeetCode is concerned; this solution always
  returns the smaller index first.

## Approach

1. Keep an empty dictionary `seen` mapping `value → index` for elements
   already scanned.
2. For each `value` at `index`, compute its complement `target - value`.
3. If the complement is a key in `seen`, the partner was found at
   `seen[complement]` — return `[seen[complement], index]` immediately.
4. Otherwise insert `seen[value] = index` and move to the next element.
5. If the loop ends without a hit, raise `ValueError` — the input violated
   the "exactly one pair" guarantee.

No sorting, no nested loop: one pass over the input, one hash lookup per
element.

## Why this approach works

Every pair `(i, j)` with `i < j` is examined exactly at the moment the scan
reaches `j`: at that point `i` has already been stored, so the check
`target - nums[j] in seen` succeeds **iff** `nums[i]` is its complement. The
map therefore never needs to hold anything beyond the prefix already scanned,
and the answer is found the first time the later half of the unique pair is
reached — which is why one pass suffices and why the returned pair is always
in increasing index order.

## Complexity

- **Time:** O(n) — one pass over `nums`, and each dict membership test /
  insertion is O(1) on average.
- **Space:** O(n) — `seen` stores at most one entry per scanned element.

## Edge cases

- Empty array or a single element → no pair can exist → `ValueError`
  (LeetCode never sends these, but the function is total).
- Duplicates that form the pair: `nums = [3, 3], target = 6` → `[0, 1]`;
  the map is checked **before** the current index is stored, so index 0 is
  reused only once.
- Negative values and a negative target: `[-3, 4, 3, 90], target = 0` →
  `[0, 2]`; nothing in the algorithm assumes positivity.
- Zeros: `[0, 0], target = 0` → `[0, 1]`; the `in` test must not be replaced
  by a truthiness check on the stored index, or index `0` looks "missing".
- No valid pair → `ValueError` rather than a silent sentinel such as `[]`,
  so a broken invariant cannot be mistaken for an answer.
- Maximum constraints (`10⁴` elements, values near `±10⁹`): sums fit Python
  ints exactly, so no overflow concern.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[2, 7, 11, 15], 9` | `[0, 1]` | the statement's example |
| `[3, 2, 4], 6` | `[1, 2]` | answer is not the first two elements |
| `[3, 3], 6` | `[0, 1]` | duplicates are two distinct positions |
| `[-3, 4, 3, 90], 0` | `[0, 2]` | negatives plus a negative target |
| `[0, 0], 0` | `[0, 1]` | stored index `0` must not read as absent |
| `[], 0` | raises `ValueError` | no pair possible |
| `[1], 1` | raises `ValueError` | a single element cannot pair with itself |
| `[1, 2, 3], 100` | raises `ValueError` | no pair exists |
| 200 random arrays with a planted pair | equals brute force | differential check against `O(n²)` reference |

## What I learned

- **Pattern:** single pass with a running state — the hash map *is* the
  running state; carry the work already done instead of re-scanning.
- **Pitfall:** `if seen.get(complement):` is wrong; index `0` is falsy. Test
  membership with `in`, and read the value afterwards.
- **Differently next time:** state the invariant ("the map holds exactly the
  prefix before `index`") before coding — it makes both the duplicate case
  and the `i < j` ordering fall out for free instead of being patched on.

**Review date:** 2026-11-06 (1 day) · 2026-11-12 (7 days) · 2026-12-05 (30 days)
