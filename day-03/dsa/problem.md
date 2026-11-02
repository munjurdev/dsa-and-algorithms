# Constraint range → allowed complexity mapping

| Field | Value |
|---|---|
| Day | `day-03` |
| Track | `dsa` |
| Topic | `01-complexity-analysis` — see `resources/topics/` |
| Difficulty | Medium |
| Platform | Other (self-made) |
| URL | _none — self-made_ |

## Problem summary

Given a problem's input bound `n`, decide which complexities are still fast
enough to pass. Every candidate complexity (`O(1)`, `O(log n)`, `O(n)`,
`O(n log n)`, `O(n^2)`, `O(n^3)`, `O(2^n)`, `O(n!)`) is expressed as an
operation-count formula in `n`, and anything whose count fits a budget of
10⁸ simple operations (~1 second) is "allowed". A second entry point takes a
constraint *range* `[lo, hi]` and returns the complexities allowed for the
whole range, which is just the answer for the largest `n` in it.

### Input

- `n: int` — the problem's maximum input size; `n >= 1`.
- `lo: int`, `hi: int` — an inclusive constraint range; `1 <= lo <= hi`.

### Output

- `allowed_complexities(n)` → `list[str]` — the allowed labels, ordered from
  fastest to slowest growing.
- `allowed_for_range(lo, hi)` → `list[str]` — same, for the whole range.

## Approach

1. Fix an operation budget `BUDGET = 10**8` — roughly what one second buys.
2. Give each complexity a cost function: `1`, `log2(n)`, `n`,
   `n * log2(n)`, `n**2`, `n**3`, and guarded forms for `2**n` (returns
   `inf` past `n = 60`) and `n!` (returns `inf` past `n = 20`) so huge inputs
   never trigger an absurd computation.
3. `allowed_complexities(n)` evaluates all eight cost functions at `n` and
   keeps the labels whose cost is `<= BUDGET`, in canonical growth order.
4. `allowed_for_range(lo, hi)` validates the range and delegates to
   `allowed_complexities(hi)`: every cost function is non-decreasing in `n`,
   so the largest `n` is the binding constraint.

The mapping this produces (the deliverable of the drill):

| Largest `n` that fits | Tightest allowed complexity | Boundary arithmetic |
|---|---|---|
| 11 | `O(n!)` | 11! ≈ 4.0×10⁷, 12! ≈ 4.8×10⁸ |
| 26 | `O(2^n)` | 2²⁶ ≈ 6.7×10⁷, 2²⁷ ≈ 1.3×10⁸ |
| 464 | `O(n^3)` | 464³ = 99,897,344 |
| 10⁴ | `O(n^2)` | (10⁴)² = 10⁸ |
| ≈4.5×10⁶ | `O(n log n)` | n·log₂n = 10⁸ around there |
| 10⁸ | `O(n)` | one linear pass at the budget |
| beyond | `O(log n)` / `O(1)` | even one pass is too slow |

## Why this approach works

Every cost function is non-decreasing in `n`, so for a range `[lo, hi]` the
maximum cost over the range is the cost at `hi` — testing only `hi` is exact,
not an approximation. And the budget test `cost(n) <= 10⁸` is precisely the
definition of "fast enough": a label is allowed exactly when the worst-case
number of operations for that input size fits in the time budget.

## Complexity

- **Time:** O(1) — eight formula evaluations, each O(1), plus two guards.
- **Space:** O(1) — the returned list holds at most the 8 labels.

## Edge cases

- `n = 1` → every complexity is allowed (`log2(1) = 0`, `2¹ = 2`, `1! = 1`).
- `n = 0` or negative → `ValueError`: there is no such problem size.
- Huge `n` (e.g. 10¹⁸) → the guards return `inf` for `2^n` and `n!`, and
  `float(n)**3` stays finite, so no overflow and no absurd big-int math.
- `lo > hi` or `lo < 1` → `ValueError` from `allowed_for_range`.
- Boundary pairs: `n = 464` keeps `O(n^3)`, `n = 465` drops it; `n = 10⁸`
  keeps `O(n)`, `n = 10⁸ + 1` drops it.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `allowed_complexities(1)` | all 8 labels | smallest size allows everything |
| `allowed_complexities(10)` | all 8 labels | 10! ≈ 3.6×10⁶ fits the budget |
| `allowed_complexities(100)` | up to `O(n^3)` | 100³ = 10⁶ fits, 2¹⁰⁰ does not |
| `allowed_complexities(10_000)` | up to `O(n^2)` | exact quadratic boundary |
| `allowed_complexities(100_000)` | up to `O(n log n)` | n² = 10¹⁰ is too slow |
| `allowed_complexities(10_000_000)` | up to `O(n)` | n log n ≈ 2.3×10⁸ > budget |
| `allowed_complexities(10**9)` | `O(1)`, `O(log n)` | a single linear pass exceeds budget |
| `allowed_complexities(464)` / `(465)` | `O(n^3)` present / absent | exact cubic boundary |
| `allowed_for_range(1, 100_000)` | `= allowed_complexities(100_000)` | range bounded by its largest n |
| `allowed_complexities(0)` | raises `ValueError` | no such problem size |
| `allowed_for_range(10, 5)` | raises `ValueError` | inverted range |

## What I learned

- **Pattern:** constraints first — read `n`, derive the allowed complexity,
  then design; this mapping is that step made mechanical.
- **Pitfall:** `O(n log n)` survives far longer than intuition suggests
  (up to ~4.5×10⁶), while `O(n^2)` dies at just 10⁴ — guessing instead of
  computing gets the budget boundary wrong by orders of magnitude.
- **Differently next time:** express every guard as "return `inf` once the
  closed form obviously exceeds the budget" so the cost functions stay total
  and never overflow on huge inputs.

**Review date:** 2026-11-03 (1 day) · 2026-11-09 (7 days) · 2026-12-02 (30 days)
