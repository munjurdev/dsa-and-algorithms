# Python Cheatsheet for DSA

Python 3.10+. Standard library only. This is the working reference used
throughout the 30-day roadmap — skim it now, come back when stuck.

## Collections at a glance

| Type | Literals | Read | Write | Good for |
|---|---|---|---|---|
| `list` | `[1, 2, 3]` | `O(1)` by index | `O(1)` amortized `append`, `O(n)` `insert` | stacks, traversal order |
| `dict` | `{"a": 1}` | `O(1)` avg | `O(1)` avg | counting, caching, adjacency |
| `set` | `{1, 2}` | `O(1)` avg | `O(1)` avg | membership, dedupe |
| `deque` | `deque([1])` | `O(1)` ends | `O(1)` ends | queues, sliding window |
| `heapq` | heap list | `O(1)` min | `O(log n)` push/pop | priority queues |

Remember: `set`/`dict` are **unordered** — never rely on iteration order for
correctness.

## Slicing and idioms

```python
nums[::-1]          # reversed copy
nums[::2]           # every second element
nums[i:j]           # subarray, never out of range (Python clamps)
s.split(",")        # str -> list
"".join(parts)      # list -> str
sorted(nums)        # new list; nums.sort() sorts in place
enumerate(nums)     # (index, value)
zip(a, b)           # pairs, stops at shortest
any(cond(x) for x in xs)   # existential
all(cond(x) for x in xs)   # universal
sum(nums, 0)        # total
collections.Counter(nums)  # frequency map in one line
```

## Useful modules for DSA

```python
import bisect            # binary search on sorted lists: bisect_left/right
import heapq             # heappush, heappop, nlargest, nsmallest
from collections import (
    Counter, defaultdict, deque, OrderedDict
)
from itertools import (
    combinations, permutations, product, groupby, accumulate
)
from functools import lru_cache, cache, reduce, cmp_to_key
from math import inf, gcd, comb, isqrt
```

### Heap pattern

```python
import heapq
heap = []
heapq.heappush(heap, (priority, item))   # min-heap
priority, item = heapq.heappop(heap)
# max-heap: push (-priority, item)
```

### `defaultdict` / `Counter` pattern

```python
from collections import defaultdict, Counter
graph: dict[str, list[str]] = defaultdict(list)
count = Counter(nums)          # {value: frequency}
count.most_common(3)           # top 3
```

## Strings

```python
s.lower(); s.upper()
s.startswith("ab"); s.endswith("z")
s.find(sub)                    # -1 if missing (str.index raises)
ord("a") == 97; chr(97) == "a"
"".join(sorted(s))             # normalized form for anagram checks
```

## Defending against input traps

- Mutating while iterating → build a new list, or iterate over a copy.
- `list.insert(0, x)` is `O(n)` → use `deque.appendleft`.
- Default mutable argument (`def f(x=[])`) is shared state → use `None`.
- Shallow copy: `b = a[:]` or `list(a)`; deep structure needs comprehension
  (`[row[:] for row in grid]`).
- Integer division: `//` floors toward `-inf`; `/` always returns float.

## Type hints (used in every solution)

```python
def two_sum(nums: list[int], target: int) -> list[int]: ...
def bfs(start: str, graph: dict[str, list[str]]) -> dict[str, int]: ...
Node = TreeNode | None
```

## Testing a solution

```python
def solve(...) -> ...:
    ...

def main() -> None:
    assert solve([2, 7, 11, 15], 9) == [0, 1]
    assert solve([], 0) == None
    print("All tests passed.")

if __name__ == "__main__":
    main()
```

Run with `python path/to/0001-two-sum.py`.

## Debugging quick wins

```python
print(f"{nums=}")            # Python 3.8+ f-string debugging
breakpoint()                  # drop into pdb
```
