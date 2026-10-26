# 24 — Bit Manipulation

> Phase 10 · Roadmap: see `ROADMAP.md` · File: `resources/topics/24-bit-manipulation.md`

Work directly on binary representations: `O(1)` tricks that replace whole
data structures, plus subset enumeration with bit masks.

## Purpose

Bit problems are short but demand precise mental models of two's complement
and masking. In interviews they appear as "without using arithmetic
operators," single-number variants, and fast subset iteration.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| AND / OR / XOR | `^` cancels equal bits, `&` keeps shared | express "unique element" with XOR |
| Shifts | `x << 1` doubles, `x >> 1` halves | extract the k-th bit |
| Mask testing | `x & (1 << k)` checks bit k | iterate all set bits |
| Two's complement | `-x == ~x + 1` | reason about negatives |
| Bit count | `x & (x - 1)` clears the lowest set bit | count 1-bits in `O(bits)` |
| Masks as subsets | `0` to `(1 << n) - 1` enumerates all subsets | iterate `2^n` subsets fast |

## Key patterns

1. **XOR everything** — the element appearing once survives (`O(1)` space).
2. **Bit count parity** — track seen state with a mask instead of a set.
3. **`(mask >> i) & 1`** — test membership of item `i` in a subset.
4. **Clear lowest bit** — `x &= x - 1` for counting and flag removal.

## Complexity expectations

- Most bit operations: `O(1)` per op; subset enumeration: `O(2^n · n)` with
  masks, `O(2^n)` when only the outer loop is needed.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | XOR cancellation |
| 2 | [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | `x & (x - 1)` trick |
| 3 | Subsets as bit masks | Medium | enumerate all `2^n` subsets |

## Prerequisites and follow-ups

- **Before this:** `00-python-fundamentals` (ints are unbounded in Python),
  `06-hashing` (contrast space trade-offs).
- **Next:** `25-intervals`.

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
