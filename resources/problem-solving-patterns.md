# Problem-Solving Patterns

A pattern is a reusable shape of solution. Learn to **spot which pattern the
problem is asking for** — that skill matters more than any single trick.
Cross-reference: each pattern maps to its roadmap phase in `ROADMAP.md`.

## The universal 5-step routine

1. **Restate** the problem in your own words; write down input/output types.
2. **Enumerate examples** — typical, edge, and a large one.
3. **Brute force first** (verbally, with complexity) — this is your baseline.
4. **Improve** — ask: repeated work? sorted? overlapping subproblems? what is
   the invariant?
5. **Complexity + edge cases** before writing a single line of code.

## Pattern catalog

| # | Pattern | Recognize it when... | Core idea | Topic |
|---|---|---|---|---|
| 1 | Hash map lookup | "find a pair / detect a duplicate / two sum" | trade space for `O(1)` lookups | [`06-hashing`](topics/06-hashing.md) |
| 2 | Two pointers | sorted input, or pair/triple searching | move ends based on a comparison | [`07-two-pointers`](topics/07-two-pointers.md) |
| 3 | Prefix sum | many range-sum queries, subarray sums | precompute cumulative, answer in `O(1)` | [`08-prefix-sum`](topics/08-prefix-sum.md) |
| 4 | Sliding window | longest/shortest subarray with a constraint | expand right, shrink left, keep window valid | [`09-sliding-window`](topics/09-sliding-window.md) |
| 5 | Binary search on answer | "minimize the maximum / feasible in O(n)" | search the value space with a predicate | [`10-binary-search`](topics/10-binary-search.md) |
| 6 | Fast & slow pointers | cycle detection, linked-list middle | Floyd's tortoise and hare | [`11-linked-list`](topics/11-linked-list.md) |
| 7 | Monotonic stack | "next greater element", histogram | keep candidates in increasing/decreasing order | [`12-stack`](topics/12-stack.md) |
| 8 | Monotonic deque | max over all subarrays of size k | keep window extremes at the ends | [`13-queue-and-deque`](topics/13-queue-and-deque.md) |
| 9 | Recursion + base case | problem reduces to a smaller version | define and trust the smaller case | [`14-recursion`](topics/14-recursion.md) |
| 10 | Backtracking | enumerate all combinations/permutations/subsets | choose → explore → un-choose | [`15-backtracking`](topics/15-backtracking.md) |
| 11 | BFS (level order) | shortest path in unweighted graph, tree levels | frontier queue, first visit wins | [`16-trees`](topics/16-trees.md), [`19-graphs`](topics/19-graphs.md) |
| 12 | DFS (recursion/stack) | connectivity, components, paths | go deep, mark visited, backtrack | [`16-trees`](topics/16-trees.md), [`19-graphs`](topics/19-graphs.md) |
| 13 | Topological sort | ordering with prerequisites, DAG | Kahn's algorithm (in-degrees) or DFS post-order | [`19-graphs`](topics/19-graphs.md) |
| 14 | Heap / PQ | repeatedly need min or max while adding | `O(log n)` extract of the global extreme | [`18-heaps-and-priority-queue`](topics/18-heaps-and-priority-queue.md) |
| 15 | Greedy choice | local optimum provably leads to global optimum | sort, then take the best-looking option | [`20-greedy`](topics/20-greedy.md) |
| 16 | Memoization / tabulation | overlapping subproblems + optimal substructure | cache results of identical states | [`21-dynamic-programming`](topics/21-dynamic-programming.md) |
| 17 | Trie | many prefix queries over a word set | share prefixes in a tree | [`22-trie`](topics/22-trie.md) |
| 18 | Union-Find | dynamic connectivity, grouping, "island merge" | union by rank + path compression | [`23-union-find`](topics/23-union-find.md) |
| 19 | Bit tricks | "without multiplication", subsets as masks | XOR cancels, `1 << n` enumerates subsets | [`24-bit-manipulation`](topics/24-bit-manipulation.md) |
| 20 | Interval merge / sweep | overlapping ranges, union of intervals | sort by start, merge, or sweep events | [`25-intervals`](topics/25-intervals.md) |

## Choosing between neighbors

- **Two pointers vs sliding window:** pointers that *cross once* on a sorted
  array = two pointers; pointers that maintain a *constraint while moving in
  one direction* = window.
- **Binary search vs hash map:** need order or a monotone predicate →
  binary search; need membership/count → hash map.
- **BFS vs DFS:** shortest unweighted path → BFS; exhaustive feasibility /
  components → DFS. Both are `O(V + E)`.
- **Greedy vs DP:** greedy never revisits a decision; DP stores state for
  choices it might regret. If you cannot prove the greedy choice property,
  use DP.
- **Memo vs tabulation:** memo mirrors your recursion (easier to derive);
  tabulation is iterative (better constants, no stack overflow).

## Template hooks

- Backtracking skeleton → `templates/problem-template.py` (fill `Approach`
  with choose/explore/un-choose).
- Topic-specific problem lists → each `NN-*/README.md`.

## Drilling schedule

1. Learn the pattern with one easy problem.
2. Solve one medium of the same pattern within 25 minutes.
3. Re-solve from a blank file 7 days later without looking.
