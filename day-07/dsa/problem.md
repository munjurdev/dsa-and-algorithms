# Two Sum — Weekly Checkpoint 01 (Closed-Notes Re-Derivation)

| Field | Value |
|---|---|
| Day | `day-07` |
| Track | `dsa` |
| Topic | `06-hashing` — see `resources/topics/` |
| Difficulty | Easy |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/two-sum/ |

## Problem summary

Given an unsorted integer array `nums` and an integer `target`, return the
**indices** of two distinct elements whose values add up to `target`. The
platform guarantees exactly one such pair; this solution does not lean on that
guarantee, it simply answers with the first pair its single pass completes. The
checkpoint twist is that the solution had to be rebuilt from a blank file with
`day-04/` closed: the only thing carried forward is the `value → index` map
pattern, not the code.

### Input

- `nums: list[int]` — `2 <= len(nums) <= 10⁴` on the platform, values
  `-10⁹ <= nums[i] <= 10⁹`, unsorted, duplicates allowed.
- `target: int` — `-10⁹ <= target <= 10⁹`.
- Here the function is total: an empty array, a single element, or a list with
  no valid pair raises `ValueError` instead of returning a sentinel.

### Output

- `list[int]` — `[i, j]` with `i < j` and `nums[i] + nums[j] == target`. When
  several pairs exist, `j` is the **smallest** index that completes a pair, and
  `i` is the most recent earlier position holding the complement.

## Approach

1. Start an empty dictionary `seen` mapping `value → latest index seen`.
2. Walk `nums` exactly once, carrying `index`.
3. Compute `complement = target - value` and test `complement in seen`:
   - **hit** → the partner is at `seen[complement]`, which is earlier than
     `index`; return `[seen[complement], index]`;
   - **miss** → store `seen[value] = index` and continue.
4. If the loop finishes, no pair exists → `ValueError`.

There is no sorting, no second pass, and no nested loop. The map is the only
state the algorithm carries.

## Why this approach works

**Prefix invariant:** before processing `index`, `seen` holds exactly
`{nums[k]: latest k}` for `k < index`. So the membership test at `index` is true
**iff** some earlier position holds the complement — and then the two indices
are distinct and their values sum to `target`. That proves every returned pair
is valid.

**Completeness:** if any valid pair `(i, j)` with `i < j` exists, then when the
scan reaches `j`, index `i` has already been stored, so the test at `j` cannot
miss. Hence the only way to reach the `raise` is that no pair exists.

**"First" is the earliest later index.** The scan returns at the first index
that completes *any* pair, so `j` is minimal by construction. Among earlier
positions holding the complement, overwriting the map on every occurrence means
`seen[complement]` is the most recent one — which is the exact pair the
brute-force reference finds when it scans leftwards from `j - 1`.

**Why `in` and not truthiness.** `if seen.get(complement):` is the classic bug
here: index `0` is falsy, so the pair `[0, j]` would be missed. Membership and
value lookup are kept separate for that reason.

## Complexity

- **Time:** O(n) — one pass over `nums`; each dict membership test and
  insertion is O(1) on average. The dict is never re-scanned.
- **Space:** O(n) — `seen` holds at most one entry per distinct value, so at
  most `n` entries; the returned pair is O(1).

## Edge cases

- Empty array or a single element → `ValueError`; no two distinct indices exist.
- Duplicates that form the pair: `[3, 3], 6` → `[0, 1]`; the test happens before
  the store, so one position is never reused.
- Three equal values: `[3, 3, 3], 6` → `[0, 1]`; the map overwrites, but the
  first completing index still wins.
- Zeros: `[0, 0], 0` → `[0, 1]`; the stored index `0` must not read as absent.
- Complement zero late in the list: `[0, 4, 3, 0], 0` → `[0, 3]`.
- Negative values and negative targets: `[-1, -2, -3, -4, -5], -8` → `[2, 4]`
  (`-3 + -5`); nothing assumes positivity.
- Several valid pairs: `[1, 2, 3, 4, 5], 5` → `[1, 2]` (right index 2 beats the
  `[0, 3]` and `[3, 4]` options); `[2, 2, 1], 4` → `[0, 1]`.
- No pair at all → `ValueError` rather than `[]`, so a broken input assumption
  cannot masquerade as an answer.
- Input is not mutated: the function never sorts or edits `nums`.
- Maximum sizes: 10⁴ elements and sums near `±2·10⁹` stay exact in Python ints,
  so no overflow path exists.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[2, 7, 11, 15], 9` | `[0, 1]` | the statement's example |
| `[3, 2, 4], 6` | `[1, 2]` | answer is not the first two elements |
| `[3, 3], 6` | `[0, 1]` | duplicates are two distinct positions |
| `[3, 3, 3], 6` | `[0, 1]` | overwriting must not shift the answer |
| `[0, 0], 0` | `[0, 1]` | index `0` must not read as absent |
| `[0, 4, 3, 0], 0` | `[0, 3]` | a late complement of zero |
| `[-3, 4, 3, 90], 0` | `[0, 2]` | negatives with a zero target |
| `[-1, -2, -3, -4, -5], -8` | `[2, 4]` | negative target |
| `[1, 2, 3, 4, 5], 5` | `[1, 2]` | earliest completing index wins |
| `[2, 2, 1], 4` | `[0, 1]` | several pairs, first right index |
| `[7, 11, 2, 15], 9` | `[0, 2]` | unsorted input, caller's list untouched |
| `[], 0`, `[1], 1`, `[1, 2, 3], 100` | raises `ValueError` | no pair possible |
| every array of length 2–4 over `-2…2`, targets `-4…4` | equals a brute-force pair reference | exhaustive differential check |
| 300 random arrays with a planted pair | valid indices, correct sum | randomized check |

## What I learned

- **Pattern:** the hash map *is* the running state — carry the prefix's work
  instead of re-scanning it, and the whole problem collapses to one pass.
- **Pitfall:** correctness of "exactly one pair" and correctness of "first
  pair" are different claims. The platform only promises the former; the
  overwrite-on-duplicate plus return-on-first-hit rule is what makes the latter
  true, and only the differential test against the brute-force reference proved
  the two agree.
- **Differently next time:** state the map's invariant ("`seen` maps each value
  to its latest index among `k < index`") before typing — it settles the
  duplicate, zero-index, and ordering questions in one sentence each.

**Review date:** 2026-11-10 (1 day) · 2026-11-16 (7 days) · 2026-12-09 (30 days)
