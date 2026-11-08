# Merge Sort vs `sorted()` (Self-Made)

| Field | Value |
|---|---|
| Day | `day-06` |
| Track | `algorithms` |
| Topic | `05-sorting` — see `resources/topics/` |
| Difficulty | Medium |
| Platform | Other (self-made exercise) |
| URL | _none — derived from the roadmap row for Day 06_ |

## Problem summary

Implement merge sort from scratch and prove it correct against Python's
`sorted()` (Timsort) with randomized differential tests. The exercise is not
just "does it produce the same list": it also checks that the sort is
**stable**, that it does not mutate its input, and that the number of
comparisons stays inside the `n ⌈log₂ n⌉` bound the complexity derivation
predicts. Finally, the two sorts are compared on how they behave — merge sort's
time is uniform at every level, Timsort exploits existing runs.

### Input

- `values: Sequence[T]` — any sequence of mutually comparable elements; tests
  use `int`s and `(key, tag)` tuples. At least `0` elements.
- Empty and single-element sequences are valid input.
- Elements only need to support `<=`; nothing else is assumed.

### Output

- `list[T]` — a **new** list holding the same elements in non-decreasing order.
  The input sequence is never modified.
- The optional `comparisons: list[int]` argument receives the number of
  element-to-element comparisons performed, so the `n ⌈log₂ n⌉` bound can be
  tested rather than asserted on faith.

## Approach

1. **Base case:** a sequence of length `0` or `1` is already sorted — return a
   copy of it.
2. **Divide:** split at `middle = len(values) // 2` and sort each half with the
   same function.
3. **Conquer:** merge the two sorted halves with two indices:
   - while both halves have unread elements, compare their heads and append the
     smaller one (taking the **left** element on a tie);
   - when one half is exhausted, append the rest of the other unchanged.
4. Return the merged list. The `sorted()` call in the tests is the oracle, never
   part of the implementation.

## Why this approach works

**Correctness by induction on length.** Lengths `0` and `1` are sorted. For
`n >= 2`, the recursive calls return sorted halves by assumption; the merge
keeps the merged output sorted because at each step the smallest unread element
of the whole input is the smaller of the two heads (each half is sorted, so
each head is its minimum). Appending the remainder of the exhausted half is safe
for the same reason.

**Stability.** Choosing the left element when the heads compare equal means
equal keys are emitted in original order: the left half holds the earlier
positions, so no equal pair is ever swapped. This is exactly the property
Timsort also has, so the differential test on tagged tuples is meaningful.

**The comparison bound.** The recursion tree has `⌈log₂ n⌉` levels, and merging
one level's lists touches each element once, performing at most `n` comparisons
per level (`n - 1` in practice per merge, summed over the level to at most `n`).
So the total is at most `n ⌈log₂ n⌉` — the test asserts this rather than
trusting it.

## Complexity

- **Time:** O(n log n) — `T(n) = 2·T(n/2) + O(n)`; `⌈log₂ n⌉` levels of linear
  merging. Every case (sorted, reversed, random) costs the same, which is where
  merge sort beats Timsort's *worst* case only in predictability, not in order.
- **Space:** O(n) peak auxiliary for the merged lists at one point in time,
  plus O(log n) recursion depth. Slicing `values[:middle]` copies, so total
  allocation over the whole run is O(n log n) even though the peak is O(n).
- **Comparison note:** `sorted()` is Timsort — stable, O(n log n) worst case,
  O(n) time on already-sorted or run-rich input, O(n) auxiliary in the worst
  case. The differential test only claims equality of *results*, not of costs.

## Edge cases

- Empty input `[]` → `[]`; never indexes `values[0]`.
- Single element `[3]` → `[3]`; the base case returns a copy, not the same list.
- Duplicates `[2, 2, 1, 1]` → `[1, 1, 2, 2]`; ties are not dropped.
- All equal `[7, 7, 7, 7]` → unchanged, and the merge takes every tie from the
  left, so stability holds trivially.
- Already sorted `[1, 2, ..., n]` and strictly reversed input: both are
  `O(n log n)` here, which is the point of the uniform-cost claim.
- Negative numbers and mixed signs: only `<=` is used, so ordering is normal.
- Odd lengths: the split is `n // 2` / `n - n // 2`, so the right half is the
  larger one; the recursion still bottoms out correctly.
- Non-mutating: passing a list must leave it in its original order, and the
  returned list must not be the input object.
- Stability: `[(1, "a"), (1, "b"), (0, "c")]` → `[(0, "c"), (1, "a"), (1, "b")]`.
- Large input (`10⁴` values): recursion depth is about 14, so no stack risk.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[3, 1, 2]` | `[1, 2, 3]` | smallest real merge |
| `[5, 2, 9, 1, 5, 6]` | `[1, 2, 5, 5, 6, 9]` | duplicates survive |
| `[]` | `[]` | base case on empty input |
| `[3]` | `[3]` | base case on one element |
| `[7, 7, 7, 7]` | `[7, 7, 7, 7]` | all ties, stability trivially checked |
| `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` | already sorted |
| `[5, 4, 3, 2, 1]` | `[1, 2, 3, 4, 5]` | fully reversed |
| `[-3, 0, -1, 2]` | `[-3, -1, 0, 2]` | negatives and zero |
| `[(1, "a"), (1, "b"), (0, "c")]` | `[(0, "c"), (1, "a"), (1, "b")]` | stable on equal keys |
| 500 random lists, length `0…60`, values `-50…50` | equal to `sorted()` | randomized differential |
| the same input passed to `merge_sort` twice | input list unchanged, results are new objects | no mutation |
| random lists of length `2…256` | comparisons `<= n · ⌈log₂ n⌉` | confirms the derivation |
| `10⁴` random values | equal to `sorted()` | constraint-size sanity check |

## What I learned

- **Pattern:** divide and conquer has one shape — make the problem smaller,
  solve the parts, and combine with work linear in the part size. The merge step
  is the entire algorithm; the recursion is bookkeeping.
- **Pitfall:** `left[i] < right[j]` looks harmless and quietly destroys
  stability; `<=` is the correct comparison when the left run comes first. Also,
  forgetting to drain the leftover tail of the longer half loses elements.
- **Differently next time:** count comparisons inside `_merge` (passing a counter
  list) instead of only quoting `O(n log n)` — the `n ⌈log₂ n⌉` assertion turns
  a memorized complexity claim into something the tests can fail on.

**Review date:** 2026-11-09 (1 day) · 2026-11-15 (7 days) · 2026-12-08 (30 days)
