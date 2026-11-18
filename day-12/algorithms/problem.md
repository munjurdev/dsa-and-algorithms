# Koko Eating Bananas

| Field | Value |
|---|---|
| Day | `day-12` |
| Track | `algorithms` |
| Topic | `10-binary-search` (binary search on the answer) — see `resources/topics/` |
| Difficulty | Medium |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/koko-eating-bananas/ |

## Problem summary

There are `n` piles of bananas and `h` hours. Each hour Koko picks one pile and
eats up to `k` bananas from it; if the pile holds fewer than `k`, she finishes
it and (by the statement's rules) spends the rest of that hour idle rather than
starting another pile. Return the smallest integer `k` that lets her clear
every pile within `h` hours. The answer is not in the input array at all — it
must be searched in the space of possible speeds `1..max(piles)`.

### Input

- `piles: list[int]` — `1 <= len(piles) <= 10⁴`, `1 <= piles[i] <= 10⁹` on the
  platform; this implementation also accepts an empty list.
- `h: int` — `len(piles) <= h <= 10⁹`. A smaller `h` is impossible (one pile
  costs at least one hour), so this implementation raises `ValueError`
  instead of returning a meaningless speed.

### Output

- `int` — the minimum feasible `k`; `0` for an empty `piles`.

## Approach

1. Handle the impossible cases: empty `piles` → `0`; `h < len(piles)` →
   `ValueError`.
2. Define `hours_needed(k) = Σ ⌈pile / k⌉` — computed as `(pile + k - 1) // k`
   with integer arithmetic. Each pile's partial last hour cannot spill over
   into the next pile.
3. Binary search the answer with `lo, hi = 1, max(piles)`:
   - `mid = (lo + hi) // 2`;
   - if `hours_needed(mid) <= h` the speed works, but a slower one might too →
     `hi = mid`;
   - else it is too slow → `lo = mid + 1`.
4. Return `lo` once `lo == hi` — the smallest feasible speed.

The feasibility predicate is `O(n)`, and it is evaluated `O(log max(piles))`
times.

## Why this approach works

**Invariant (one sentence):** at every step the answer lies in `[lo, hi]`, with
`lo` never known-feasible and `hi` always known-feasible.

*The predicate is monotone.* For a fixed pile, `⌈pile / k⌉` is
non-increasing in `k`; a sum of non-increasing functions is non-increasing. So
if speed `k` finishes in time, every `k' > k` does as well, and the feasible
speeds form the suffix `[k*, max(piles)]` of the search range. Binary search on
a boolean predicate over a sorted suffix finds its first element — that is
exactly `k*`.

*The upper bound is feasible.* `k = max(piles)` eats every pile in one hour, so
`hours_needed(max(piles)) = n <= h` by the precondition; the search never
starts above the answer's range.

*The narrowing is conservative.* `hi = mid` only when `mid` is feasible (keeping
`hi` feasible, since the *first* feasible speed is `<= mid`), and `lo = mid + 1`
only when `mid` is infeasible (so the answer is strictly above it). Each
iteration removes `mid` from the candidate set, the interval strictly shrinks,
and the loop ends at the single remaining speed, which is feasible — the
minimum.

## Complexity

- **Time:** O(n log m) — `m = max(piles) <= 10⁹`, so about 30 feasibility
  passes, each a single `O(n)` sum; total well under the platform limit.
- **Space:** O(1) — two bounds, a midpoint, and a running hour total; no
  per-speed table is materialized.

## Edge cases

- `piles == []` → `0` (nothing to eat, any speed works vacuously).
- `h < len(piles)` → `ValueError`; no speed can eat two piles in one hour, so
  there is no answer to return.
- `h == len(piles)` → the answer is `max(piles)` (each pile in exactly one hour).
- `h >= sum(piles)` → the answer is `1` (one banana per hour clears everything).
- Single pile: `[7]`, `h = 1` → `7`; `[7]`, `h = 100` → `1`;
  `[312884470]`, `h = 312884469` → `2` (tight ceiling makes the answer `2`,
  not `1`).
- Large values: `[1000000000]`, `h = 2` → `500000000`; ceiling division must
  not be replaced by `pile // k`, which would under-count every partial hour.
- Duplicate piles (`[805306368] * 3`) → handled; the sum is over piles, not
  distinct sizes.
- Maximum `h` (`10⁹`) → the search still runs ~30 passes; final `lo = 1`
  possible only when the total fits exactly.
- Answers that are not pile sizes: `[30,11,23,4,20]`, `h = 6` → `23`, a value
  that happens to be a pile here; `[3,6,7,11]`, `h = 8` → `4`, which would be
  missed entirely by a binary search over the sorted piles themselves.
- `h` is not mutated, `piles` is not sorted or modified.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[3,6,7,11]`, `8` | `4` | the statement's example |
| `[30,11,23,4,20]`, `5` | `30` | tight budget: one hour per pile |
| `[30,11,23,4,20]`, `6` | `23` | the answer is not a pile boundary |
| `[]`, `5` | `0` | nothing to eat |
| `[7]`, `1` | `7` | single pile, single hour |
| `[7]`, `100` | `1` | generous budget |
| `[1,1,1,1]`, `4` | `1` | unit piles |
| `[3,6,7,11]`, `4` | `11` | `h == len(piles)` → max pile |
| `[805306368]*3`, `3` | `805306368` | `h == len(piles)` at platform scale |
| `[312884470]`, `312884469` | `2` | ceiling matters at the boundary |
| `[1000000000]`, `2` | `500000000` | half of the platform maximum |
| `[1000000000]`, `1000000000` | `1` | one banana per hour suffices |
| `[805306368]*3`, `1000000000` | `3` | huge `h` collapses to three hours |
| `[3,6,7]` with `h = 0, 1, 2` | `ValueError` | impossible budgets rejected |
| 40 random pile lists of size 1–3 with values 1–9, every `h` in `len..4·len+1` | equals the linear scan | exhaustive differential check |
| 300 random lists (size 1–20, values 1–500) with `h` in `len..len+200` | equals the linear scan | randomized differential check |

## What I learned

- **Pattern:** "minimize the maximum / smallest speed that works" is a
  monotone-predicate search. The hard part is not the binary search but writing
  the predicate down first (`Σ ⌈p/k⌉ <= h`) and checking that it is monotone —
  once that is proven, the loop is mechanical.
- **Pitfall:** two off-by-one traps hide here. `pile // k` instead of `⌈pile/k⌉`
  under-counts partial hours (fails `h = len(piles)` cases), and `while lo <=
  hi` with `hi = mid - 1` on a feasible midpoint returns the wrong speed
  because `mid` is then discarded even though it may be the answer. The
  half-open `while lo < hi` / `hi = mid` form is the one that matches the
  "first feasible value" question.
- **Differently next time:** write the feasibility predicate and a linear-scan
  oracle *before* the search, then differential-test — the oracle found my
  ceiling-division mistake before I had even finished the bounds.

**Review date:** 2026-11-19 (1 day) · 2026-11-25 (7 days) · 2026-12-18 (30 days)
