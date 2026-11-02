# Classify 10 snippets + justify `list.append` amortization

| Field | Value |
|---|---|
| Day | `day-03` |
| Track | `algorithms` |
| Topic | `01-complexity-analysis` — see `resources/topics/` |
| Difficulty | Easy |
| Platform | Other (self-made drill) |
| URL | _none — self-made_ |

## Problem summary

Ten short Python functions, each to be classified by its worst-case Big-O
with a one-line justification — the graded deliverable is 10/10 correct,
every answer backed by a single sentence. The second part is the classic
amortization question: prove that `list.append` is `O(1)` even though it
sometimes has to copy the whole list. `solution.py` contains the ten
snippets plus a small `ast`-based classifier that re-derives each answer
mechanically, so the table can be checked instead of trusted.

### Input

- `code: str` — a source snippet containing exactly one function definition
  (the classifier parses it with `ast.parse`).
- `n: int` — the input size assumed for every snippet's list argument.

### Output

- `classify(code)` → `str` — a label such as `"O(n^2)"`.
- `total_copies(n)` → `int` — element copies made while growing a list to
  `n` appends under the doubling strategy.
- `justify_append_amortization()` → `str` — the one-line amortization
  argument.

## Approach

1. Classify each snippet by hand: find the innermost statement's cost, then
   multiply by the loop nesting (a loop over `n` elements multiplies by `n`;
   a `while` that halves its induction variable multiplies by `log n`;
   sequential statements take the faster-growing one).
2. Encode the same rules in `classify()`: parse with `ast`, and compute a
   cost pair `(a, b)` meaning `n^a · (log n)^b` —
   - loops multiply the body by `(1, 0)`, a halving `while` by `(0, 1)`;
   - sequential statements take the lexicographic max of their pairs;
   - `sorted(...)` / `.sort()` cost `(1, 1)`, a list membership test costs
     `(1, 0)`, hash-collection membership (`set(...)`, `{...}`, `dict(...)`)
     costs `(0, 0)`;
   - any call outside the known list raises `ValueError` rather than
     silently guessing.
3. `main()` classifies all ten snippets, requires every expected label to
   match (10/10) and every justification to be a single non-empty line.
4. For the amortization drill, `total_copies(n)` simulates capacity doubling
   (grow 1 → 2 → 4 → …) and counts the copied elements; `main()` asserts the
   total never exceeds `2n`, which is the proof.

### The ten classifications

| # | Snippet | Expected | One-line justification |
|---|---|---|---|
| 1 | `return len(xs)` | `O(1)` | `len()` reads a field stored on the list, so it never scans. |
| 2 | `return xs[0] + xs[-1]` | `O(1)` | Indexing is address arithmetic: one step regardless of size. |
| 3 | binary search (`while` with `mid = (lo+hi)//2`) | `O(log n)` | Each comparison halves the remaining range, so ~log₂ n steps. |
| 4 | single loop accumulating a sum | `O(n)` | One pass with constant work per element. |
| 5 | early-exit linear search over `enumerate(xs)` | `O(n)` | Worst case scans every element once; Big-O is the worst case. |
| 6 | two sequential loops over `xs` | `O(n)` | Two linear passes are still linear; constant factors drop out. |
| 7 | nested loop counting pairs | `O(n^2)` | The inner loop runs once per outer element: n·n pairs. |
| 8 | `[x for x in xs if x in seen]` with `seen` a list | `O(n^2)` | Each of the n membership tests scans the list it checks against. |
| 9 | `return sorted(xs)` | `O(n log n)` | A comparison sort performs Θ(n log n) comparisons. |
| 10 | loop appending `sorted(xs)` each iteration | `O(n^2 log n)` | n iterations × an n log n sort each. |

## Why this approach works

Costs form a small algebra: for two terms `n^a·log^b n` and `n^c·log^d n`,
their sum is dominated by the lexicographically larger `(a, b)` (the faster
growth swamps the slower one) and their product adds the pairs. A loop over
`n` elements multiplies its body exactly once per element, so nesting loops
adds `(1, 0)` per level — which is why loop nesting depth maps directly to
the exponent of `n`. `list.append` is constant *amortized* because capacity
doubling copies at most `1 + 2 + 4 + … ≤ 2n` elements over `n` appends, so
the average copy cost per append is under 2 — a constant.

## Complexity

- **Time:** O(S) — one `ast` pass per snippet, S = total source size; the
  ten-snippet run is effectively constant.
- **Space:** O(D) — recursion depth D bounded by the snippet's AST depth
  (plus O(D) for `ast.parse`'s own stack).

## Edge cases

- A call outside the known list (`mystery(xs)`) → `ValueError`: the
  classifier fails loudly instead of returning a wrong label.
- Membership on a hash collection (`x in {1, 2, 3}`) is `O(1)`, not `O(n)`
  — the classifier special-cases `set`/`dict`/`{...}`; on a plain name it
  assumes a list, the conservative reading. Note `x in set(xs)` inline is
  still `O(n)` overall, because the set itself is rebuilt every iteration.
- A `while` loop with no halving is treated as linear — the halving rule
  only fires on `//`, `/`, or `>>` by a constant.
- Early exit does not lower Big-O: snippet 5 is `O(n)` because the worst
  case (absent target) is the one that counts.
- `total_copies(0) == 0` and `total_copies(1) == 0` — the first allocation
  copies nothing.
- Snippets without a function definition → `ValueError` from `classify`.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `classify()` on each of the 10 snippets | matches all 10 expected labels | the completion criterion: 10/10 |
| `classify` on `if x in {1, 2, 3}` comprehension | `O(n)` | hash membership stays linear |
| `classify` on an unknown call | raises `ValueError` | no silent guessing |
| `total_copies(0)` / `total_copies(1)` | `0` / `0` | first allocation copies nothing |
| `total_copies(5)` | `7` | copies 1 + 2 + 4 while growing 1→2→4→8 |
| `total_copies(n) <= 2 * n` for n up to 10 000 | holds | the amortization bound |
| `justify_append_amortization()` | ends with `amortized O(1).` | the written justification |

## What I learned

- **Pattern:** loop nesting depth *is* the exponent of `n` — count the
  innermost statement's cost, multiply outward, never count loop headers.
- **Pitfall:** "it exits early" is not a complexity argument; worst case
  decides Big-O, and sequential passes multiply nothing — they add.
- **Differently next time:** write the classifier before grading myself, so
  the expected table is machine-checked instead of hand-waved; state the
  `2n` copy bound as an inequality up front rather than after simulating.

**Review date:** 2026-11-03 (1 day) · 2026-11-09 (7 days) · 2026-12-02 (30 days)
