# FizzBuzz + top-k frequency drill

| Field | Value |
|---|---|
| Day | `day-01` |
| Track | `algorithms` |
| Topic | `00-python-fundamentals` — see `resources/topics/` |
| Difficulty | Easy |
| Platform | Other (self-made drill) |
| URL | _none — self-made_ |

## Problem summary

Two-part control-flow and counting drill. Part A: generate the FizzBuzz
sequence for 1..n, where multiples of 3 say "Fizz", multiples of 5 say
"Buzz", and multiples of both say "FizzBuzz"; every other number says itself.
Part B: given a list of words and an integer k, return the k most frequent
words ordered by descending frequency, with an alphabetical tie-break so the
answer is deterministic.

### Input

- Part A — `limit: int`; inclusive upper bound (0 or less gives an empty
  sequence).
- Part B — `items: list[str]` (may be empty, may contain duplicates) and
  `k: int` ≥ 0, the number of distinct words to return.

### Output

- Part A — `list[str]` with exactly `limit` entries (`[]` for `limit < 1`).
- Part B — `list[str]` of up to `k` words, most frequent first.

## Approach

**FizzBuzz**

1. Loop `number` over `range(1, limit + 1)`.
2. Test divisibility in order: `% 15` first, then `% 3`, then `% 5`.
3. Append `"FizzBuzz"` / `"Fizz"` / `"Buzz"` / `str(number)` — always a
   string, so the list has a single element type.

**Top-k frequency**

1. `Counter(items)` counts every word in one pass.
2. `sorted(counts.items(), key=lambda entry: (-entry[1], entry[0]))` — the
   negative count sorts descending, the word itself breaks ties
   alphabetically.
3. Slice the first `k` entries and return just the words.

## Why this approach works

15 is the least common multiple of 3 and 5, so testing it first sends every
number divisible by both to "FizzBuzz" before the narrower `% 3` and `% 5`
branches can claim it — that branch order *is* the correctness argument for
FizzBuzz. For top-k, the key `(-count, word)` is a total order: every
distinct word ranks exactly once with no ties left, so the prefix of length
`k` is always the same well-defined answer.

## Complexity

- **FizzBuzz — Time:** O(n) — one iteration per number, O(1) work each.
- **FizzBuzz — Space:** O(n) — the output list stores n strings.
- **Top-k — Time:** O(m + u log u) — one pass of m counts, then sorting the
  u distinct words.
- **Top-k — Space:** O(u) — one counter entry per distinct word, plus at most
  k words of output.

## Edge cases

- `limit = 0` (or negative) → `[]`; the loop body never runs.
- `limit = 1` → `["1"]`; no special case needed.
- `items = []` → `[]`; the counter is empty and the sort is trivial.
- `k = 0` → `[]`; `k` larger than the number of distinct words → all of them
  (slicing never raises).
- Equal frequencies → alphabetical order, so tests stay deterministic.
- One word repeated → that word alone regardless of `k`.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `fizz_buzz(15)` | `["1","2","Fizz","4","Buzz",…,"FizzBuzz"]` | all three branches hit |
| `fizz_buzz(0)` | `[]` | empty input |
| `fizz_buzz(1)` | `["1"]` | single element |
| `top_k_frequent(["a","b","a","c","b","a"], 2)` | `["a","b"]` | typical ranking |
| `top_k_frequent([], 3)` | `[]` | empty input |
| `top_k_frequent(["b","a","b","a"], 2)` | `["a","b"]` | tie → alphabetical |

## What I learned

- **Pattern:** guard clause first (`k <= 0` returns early), happy path flat.
- **Pitfall:** testing `% 3` before `% 15` mislabels 15, 30, … as "Fizz".
- **Differently next time:** fix the tie-break rule before writing the sort —
  a deterministic order is what makes a frequency test trustworthy.

**Review date:** 2026-11-02 (1 day) · 2026-11-08 (7 days) · 2026-12-01 (30 days)
