# Complexity Analysis Cheatsheet

Big-O describes how runtime (or memory) grows as input size `n` grows.
Constants and lower-order terms are dropped: `3n + 20` is `O(n)`.

## Common growth rates

| Name | Example | n = 1,000 runs about... |
|---|---|---|
| `O(1)` | hash lookup, array index | 1 step |
| `O(log n)` | binary search | 10 steps |
| `O(sqrt(n))` | trial division to sqrt | 32 steps |
| `O(n)` | single loop, linear scan | 1,000 |
| `O(n log n)` | good sorts, efficient heap ops | 10,000 |
| `O(n^2)` | nested loops over the same input | 1,000,000 |
| `O(n^3)` | Floyd–Warshall, naive matrix multiply | 1,000,000,000 |
| `O(2^n)` | subset enumeration, naive recursion | 2^1000 — impossible |

Rule of thumb: at n = 1,000, anything past `O(n^2)` is usually too slow for
an interactive platform with a ~1–2 s limit. LeetCode-style constraints are a
direct hint:

| Constraints on `n` | Suggests |
|---|---|
| `n <= 10` | `O(2^n)` / `O(n!)` is fine |
| `n <= 100` | `O(n^3)`, `O(n^2)` |
| `n <= 1,000` | `O(n^2)` borderline; prefer `O(n log n)` |
| `n <= 100,000` | `O(n log n)` or `O(n)` |
| `n <= 10,000,000` | `O(n)`, minimal constant overhead |

## Analyzing loops

```python
for i in range(n):          # O(n)
    for j in range(i, n):    # O(n^2) total, not O(n^3) — count iterations
        work()               # O(1) each
```

- Halving loops (`while n > 1: n //= 2`) are `O(log n)`.
- Nested loops with independent bounds multiply: `O(n * m)`.
- Sorting the input once usually dominates: count it as `O(n log n)`.

## Amortized analysis

- `list.append` is `O(1)` **amortized** — occasionally the array resizes
  (`O(n)`), but the average over n appends is constant.
- Union-Find with path compression + union by rank is `O(α(n))` per op —
  effectively constant.
- State amortized vs worst case explicitly when they differ.

## Space complexity

- Count **auxiliary** space, not the input itself (unless told otherwise).
- Recursion stack counts: a recursion depth of `n` is `O(n)` space.
- A memo table of size `n` is `O(n)` even if the recursion tree is `O(2^n)`.

```python
def helper(i: int, memo: dict[int, int]) -> int: ...   # O(n) time extra stack + O(n) memo
```

## The master theorem (divide and conquer)

For `T(n) = a·T(n/b) + O(n^d)`:

- `d < log_b a` → `O(n^(log_b a))`
- `d = log_b a` → `O(n^d · log n)`
- `d > log_b a` → `O(n^d)`

Merge sort: `a=2, b=2, d=1` → `O(n log n)`.

## Worked micro-examples

```python
# O(n) — each element visited once
seen = set()
for x in nums:
    seen.add(x)

# O(n log n) — sort dominates the following scan
return sorted(nums)[k]

# O(n) average / O(n^2) worst — hash collisions; assume average in interviews
def has_duplicate(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)

# O(log n) — search space halves each step
def lower_bound(a: list[int], target: int) -> int:
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

## How to write the analysis in a solution file

1. Name the dominant operation (e.g. "each element enters and leaves the
   window at most once").
2. Multiply by the per-operation cost.
3. State best/average/worst when they differ.
4. Say what the space is used for: "hash map holds at most k distinct keys."
