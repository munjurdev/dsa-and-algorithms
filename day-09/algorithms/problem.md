# Product of Array Except Self

| Field | Value |
|---|---|
| Day | `day-09` |
| Track | `algorithms` |
| Topic | `08-prefix-sum` (prefix/suffix products) — see `resources/topics/` |
| Difficulty | Medium |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/product-of-array-except-self/ |

## Problem summary

For each index `i`, return the product of every element of `nums` **except**
`nums[i]`. The answer must be produced in `O(n)` time **without division** and
with `O(1)` extra space beyond the output array. The ban on division is what
makes zeros interesting: with division you would need a zero count and a
nonzero product, and edge cases for one zero, two zeros, and no zeros.

### Input

- `nums: list[int]` — `2 <= len(nums) <= 10⁵` on the platform, values
  `-30 <= nums[i] <= 30`, possibly zero or negative.
- This implementation is total: `[]` returns `[]`, and a single element
  returns `[1]` (the empty product), though the platform guarantees ≥ 2.

### Output

- `list[int]` — a new list of the same length with
  `result[i] = prod(nums[:i]) * prod(nums[i + 1:])`; zeros appear exactly when
  some **other** index holds a zero.

## Approach

The answer at each index is the product of a **prefix** and a **suffix**:
`result[i] = prefix_product(i) * suffix_product(i)`, where the prefix product
covers indices `< i` and the suffix product covers indices `> i`. Both are
computed in place in the output array, so nothing but one running scalar is
carried:

1. **Left pass** (`i = 0 … n-1`): write `result[i] = prefix`, then
   `prefix *= nums[i]`. After this pass `result[i]` holds the product of
   everything left of `i`. The first slot gets `1`, the empty product.
2. **Right pass** (`i = n-1 … 0`): multiply `result[i]` by `suffix`, then
   `suffix *= nums[i]`. Now each `result[i]` also includes everything right of
   `i`, and `suffix` is the product of the suffix.
3. Return `result`.

No division, no `math.prod` over slices, no auxiliary prefix or suffix arrays —
the output array is reused as scratch space, which is exactly why the extra
space is `O(1)`.

## Why this approach works

**Correctness by partition.** The multiset of indices other than `i` splits
into `{k : k < i}` and `{k : k > i}`. Their product is independent of order, so
multiplying the two partial products gives exactly the product of everything
except `nums[i]`. The left pass fills the first factor, the right pass
multiplies in the second; at the moment the right pass touches index `i`, the
suffix scalar is exactly `prod(nums[i+1:])`.

**No division means zeros need no branch.** The method never divides, so a
zero simply propagates through the products it belongs to:
- no zeros → every answer is the full product divided conceptually by one
  factor, computed by multiplication;
- one zero → only the zero's own slot gets the product of the nonzero
  elements, and every other slot includes the zero, hence `0`;
- two or more zeros → every answer includes at least one zero, so all are `0`.

These are consequences of the arithmetic, not cases in the code.

**Space argument.** `result` is the required output, so it is not counted.
Apart from it the algorithm uses two scalars (`prefix`, `suffix`) and one loop
index, i.e. `O(1)` extra space. Writing the left products into `result` costs
nothing extra because that space was already allocated.

**Why the empty products are `1`.** At `i = 0` there are no indices to the
left, so the prefix product must be the multiplicative identity; likewise for
the suffix at `n - 1`. That single choice also makes single-element input
return `1` naturally.

## Complexity

- **Time:** O(n) — two passes over `nums`, each doing one multiplication and
  one assignment per element.
- **Space:** O(1) auxiliary — only `prefix`, `suffix`, and loop indices beyond
  the returned list. The input is read but never mutated.

## Edge cases

- `[]` → `[]`; `[5]` and `[0]` → `[1]` (empty product).
- Two elements: `[2, 3]` → `[3, 2]`; `[0, 7]` → `[7, 0]`.
- One zero: `[1, 0]` → `[0, 1]`; `[0, 1, 2]` → `[2, 0, 0]`; in a longer array
  `[1, 2, 0, 4, 5]` → `[0, 0, 40, 0, 0]`.
- Two zeros: `[0, 0]` → `[0, 0]`; `[0, 1, 0, 2]` → all zeros, because every
  index still has another zero among the remaining elements.
- Negatives: `[-1, -2, -3, -4]` → `[-24, -12, -8, -6]`; sign is the parity of
  the negatives left out, which the products handle automatically.
- Mixed zero and negative: `[-2, 0, -3]` → `[0, 6, 0]`.
- Repeated values: `[2, 2, 2]` → `[4, 4, 4]`, not a division shortcut.
- Values up to `±30` over `10⁵` elements produce huge products, which is fine
  in Python (arbitrary-precision ints); the same algorithm in a fixed-width
  language would need a product-size check, not a logic change.
- Input list is not mutated, so callers can reuse it.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[1, 2, 3, 4]` | `[24, 12, 8, 6]` | the statement's example |
| `[-1, 1, 0, -3, 3]` | `[0, 0, 9, 0, 0]` | one zero, negatives |
| `[]` | `[]` | empty input |
| `[5]`, `[0]` | `[1]` | empty product |
| `[2, 3]` | `[3, 2]` | each answer is the other element |
| `[0, 7]` | `[7, 0]` | zero at the first index |
| `[0, 1, 2]` | `[2, 0, 0]` | one zero: its slot survives |
| `[0, 1, 0, 2]` | `[0, 0, 0, 0]` | two zeros: nothing survives |
| `[1, 2, 0, 4, 5]` | `[0, 0, 40, 0, 0]` | zero's slot gets the nonzero product |
| `[-1, -2, -3, -4]` | `[-24, -12, -8, -6]` | signs from negative parity |
| `[-2, 0, -3]` | `[0, 6, 0]` | zero plus negatives |
| `[1, 2, 3, 4, 5]` | `[120, 60, 40, 30, 24]` | longer array |
| every array of length 0–5 over `-2…2` | equals an `math.prod` oracle | exhaustive differential check |
| 400 random arrays of length 0–20 over `-4…4` | equals the oracle | randomized differential check |

## What I learned

- **Pattern:** a "product/sum of everything except me" answer is a prefix
  combined with a suffix; when the output array is allowed to be written, one
  of the two passes can be stored in it for free.
- **Pitfall:** reaching for division looks natural until zeros arrive, and then
  the code needs a zero count, a nonzero product, and three branches. The
  prefix/suffix product needs none of that — the zero handling disappears
  instead of being special-cased.
- **Differently next time:** check the empty-product identity at the boundary
  indices first (`prefix = 1` before the loop). That one decision is what makes
  single-element and first/last-slot answers correct without conditionals.

**Review date:** 2026-11-11 (1 day) · 2026-11-17 (7 days) · 2026-12-10 (30 days)
