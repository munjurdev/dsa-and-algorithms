# Subarray Sum Equals K

| Field | Value |
|---|---|
| Day | `day-09` |
| Track | `dsa` |
| Topic | `08-prefix-sum` — see `resources/topics/` |
| Difficulty | Medium |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/subarray-sum-equals-k/ |

## Problem summary

Given an integer array `nums` and an integer `k`, count the **contiguous**
subarrays whose elements sum exactly to `k`. The array may contain negative
numbers and zeros, so a sliding window is not valid — the sum does not grow
monotonically as the window expands. The intended solution rewrites the
condition in terms of prefix sums and answers it with a hash map in one pass.

### Input

- `nums: list[int]` — `1 <= len(nums) <= 2·10⁴` on the platform, values
  `-1000 <= nums[i] <= 1000`, unsorted, negatives and zeros allowed.
- `k: int` — `-10⁷ <= k <= 10⁷`.
- This implementation is total: an empty array returns `0`.

### Output

- `int` — the number of index pairs `i <= j` with
  `sum(nums[i:j + 1]) == k`. Counting is over **pairs of indices**, so equal
  values in different positions count separately.

## Approach

1. Define `prefix[j] = sum(nums[:j])`, so `prefix[0] = 0` is the empty prefix.
2. A subarray `nums[i:j]` sums to `k` exactly when
   `prefix[j] - prefix[i] == k`, i.e. `prefix[i] == prefix[j] - k`.
3. Scan once, maintaining `running = prefix[j]` and a map
   `prefix_counts: prefix value → how many indices < j have it`, seeded with
   `{0: 1}` for the empty prefix.
4. At each `value`:
   - `running += value`;
   - `count += prefix_counts.get(running - k, 0)` — every earlier prefix equal
     to `running - k` ends exactly one valid subarray at `j`;
   - increment `prefix_counts[running]`.
5. Return `count`.

No nested loops, no window, no division, and the whole array is read once.

## Why this approach works

**Bijection between subarrays and prefix pairs.** For every pair `i <= j`, the
subarray `nums[i:j + 1]` corresponds to the pair `(prefix[i], prefix[j])`, and
the map from subarray to index pair is one-to-one. So counting subarrays whose
sum is `k` equals counting indices `i < j'` (where `j' = j + 1`) with
`prefix[i] = prefix[j'] - k`. The scan visits each `j'` once and looks up how
many earlier prefixes satisfy that equation — exactly the number of valid
subarrays ending at `j' - 1`.

**The empty prefix is not an optimization, it is required.** Without
`{0: 1}`, a subarray starting at index `0` has `prefix[i] = prefix[0] = 0`,
which is never in the map, so `[1, 2, 3], 6` would return `0`. The empty
prefix is a real prefix index, and seeding it with count `1` is what makes
those subarrays countable.

**Duplicate prefix values must be counted, not overwritten.** Two equal
prefix values mean the elements between them sum to zero. Storing a count
instead of a single index is what makes `[0, 0, 0], 0` return `6` rather than
`3`. Because the update happens *after* the lookup, the current index never
pairs with itself — subarrays are non-empty by construction.

**Why not a sliding window?** With negative values, shrinking the left side can
increase the sum, so "too large → move left" is unsound. Prefix sums do not
care about sign: each index pair is examined independently.

## Complexity

- **Time:** O(n) — one pass over `nums`; each iteration does one dictionary
  lookup and one insertion, both O(1) on average.
- **Space:** O(n) — in the worst case (all prefix sums distinct) the map holds
  `n + 1` entries, including the empty prefix.

## Edge cases

- Empty array → `0`; there is no non-empty subarray.
- Single element equal to `k` → `1`; not equal → `0`.
- Subarray starting at index 0 (`[1, 2, 3], 6`) → `1`, only if the empty
  prefix is seeded.
- `k = 0` with negative values: `[1, -1, 0]` → `3` (`[1,-1]`, `[0]`,
  `[1,-1,0]`).
- Runs of zeros: `[0, 0, 0]` → `6` subarrays for `k = 0`; each zero adds a new
  equal prefix, and counts must accumulate rather than overwrite.
- All negatives: `[-1, -1, 1], 0` → `1`; the window intuition breaks, the
  prefix equation does not.
- Large magnitudes: `10⁹` and `-10⁹` are exact in Python ints, and the running
  sum can never overflow.
- Input is not mutated; the scan is read-only.
- `nums` with one element and `k = 0` when that element is `0` → `1`.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[1, 1, 1], 2` | `2` | the statement's example |
| `[1, 2, 3], 3` | `2` | `[3]` and `[1, 2]` |
| `[1, 2, 3], 6` | `1` | whole array — needs the empty prefix |
| `[3], 3` | `1` | single element starting at index 0 |
| `[0, 0, 0], 0` | `6` | every subarray of a zero run |
| `[1, -1, 0], 0` | `3` | negatives plus a zero |
| `[1, -1, 1, -1], 0` | `4` | repeated prefix values |
| `[2, -2, 2, -2], 2` | `3` | three separate odd-index starts |
| `[1, 1, 1, 1, 1], 3` | `3` | exactly the length-3 windows |
| `[], 0`, `[], 5`, `[1], 0` | `0` | no non-empty subarray |
| `[10**9, -10**9], 0` | `1` | large negative value |
| `[1, 2], 100` | `0` | target unreachable |
| every array of length 0–5 over `-2…2`, targets `-3…3` | equals an every-start brute force | exhaustive differential check |
| 400 random arrays of length 0–40 over `-5…5` | equals the brute force | randomized differential check |

## What I learned

- **Pattern:** rewrite "contiguous segment has property P" as a difference of
  two prefixes, then count matching prefixes as you go — the hash map holds
  the past, the running total holds the present.
- **Pitfall:** the empty prefix is the whole trick. Seeding `{0: 1}` is one
  line, but omitting it silently loses every subarray that starts at index 0 —
  and the statement's own examples (`[1,1,1], 2`) still pass, which is why the
  differential test targeted `k` equal to a prefix sum.
- **Differently next time:** state the equation `prefix[j] - prefix[i] == k`
  before writing code. It fixes the seed, the lookup direction, and the
  update-after-query order in one step.

**Review date:** 2026-11-11 (1 day) · 2026-11-17 (7 days) · 2026-12-10 (30 days)
