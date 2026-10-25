# Common Mistakes

A running log of mistakes I actually make — re-read before each practice
session. Add your own entries; the value is in *your* errors, not a generic
list.

## Python-specific

| Mistake | Fix |
|---|---|
| `sorted(nums, key=lambda x: ...)` on strings that need numeric order | sort by the parsed key, e.g. `key=len` or `key=int` |
| `if x in my_list` inside a loop → `O(n^2)` | use a `set` or `dict` for membership |
| Mutating a list while iterating it | iterate a copy (`for x in nums[:]`) or build a new list |
| `a = b = []` shares one list between names | `a, b = [], []` |
| `def f(x=[])` shares the default across calls | use `x: list[int] \| None = None` and create inside |
| Forgetting `list.sort()` returns `None` | `nums.sort()` in place; `sorted_nums = sorted(nums)` for a copy |
| Shallow copy of nested structures | `[row[:] for row in grid]` |
| Recursion hits Python's 1000-frame limit | set `sys.setrecursionlimit` **or** (better) convert to iteration / add memo |
| Integer `/` producing floats where `//` is meant | use `//` and be explicit about floor vs truncation |

## Algorithmic

- **Off-by-one in binary search** — settle on one convention
  (`lo, hi = 0, len(a)`; loop `while lo < hi`; return `lo`) and use it
  everywhere. Test with `len <= 1` arrays.
- **Using an index as a value** (or vice versa) — label variables
  (`target_idx`, `weight`) to keep them apart.
- **Missing the empty-input case** — check `n == 0` before loops that assume
  at least one element.
- **Wrong complexity claim** — a `set` built inside a loop is `O(n^2)`, not
  `O(n)`. Count the inner work.
- **Greedy without proof** — write down *why* the local choice is safe, or
  switch to DP.
- **Visited marking too late/too early in DFS** — mark on enqueue for BFS;
  be consistent about "in progress" vs "done" for cycle detection.
- **Forgetting to reset state** between test cases (global mutable structures).
- **Solving only the happy path** — always test: empty, single element,
  all equal, already sorted, maximum size, no-solution input.

## Process mistakes

- Reading the editorial before attempting a real attempt → you learn nothing.
- Copying code without re-deriving it → schedule an earlier review date.
- Skipping the complexity write-up → the analysis *is* the learning.
- Chasing problem count over understanding → 2 well-explained problems beat
  10 skimmed ones.
- Not logging a mistake here → the same bug will recur in three weeks.

## How to use this file

1. After every session, append anything that cost you time.
2. Before each session, skim the last two weeks of entries.
3. When an entry stops recurring for 30 days, strike it through — keep the
   record, retire the noise.
