# 00 — Python Fundamentals

> Phase 1 · Roadmap: see `ROADMAP.md` · File: `resources/topics/00-python-fundamentals.md`

Build the Python fluency that everything else in this repo assumes: you should
never be fighting the *language* while trying to solve an *algorithm*.

## Purpose

Python is the tool of record for this repository. Before touching data
structures, you must be able to index, slice, iterate, and manipulate
collections without hesitation, and know the cost of each operation.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Variables & types | Names bind to objects; everything is an object | pick the right type for a job |
| Strings | Immutable sequences of Unicode | normalize, index, and join without loops |
| Lists | Dynamic arrays, `O(1)` amortized append | slice, comprehension, in-place update |
| Dicts & sets | Hash tables with `O(1)` average lookup | count, dedupe, and map keys |
| Control flow | `for`/`while`, `if`/`elif`, comprehensions | rewrite a nested loop as a comprehension |
| Functions | First-class objects with defaults | write pure functions with type hints |
| Slicing & iteration | `enumerate`, `zip`, `any`, `all` | express scans in one line when clearer |

## Key patterns

1. **Frequency counting** — `Counter` / `defaultdict(int)` instead of manual
   loops.
2. **Build then transform** — list comprehensions for mapping/filtering.
3. **Guard clauses** — handle edge cases at the top, keep the happy path flat.

## Complexity expectations

- Know the cost of `list.append`, `list.insert(0, x)`, `x in list`,
  `x in set`, `dict[key]` — see `../complexity-cheatsheet.md`.
- Choosing `set` over `list` for membership can be the whole optimization.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | Count words in a text | Easy | dicts, `split`, frequency maps |
| 2 | FizzBuzz | Easy | control flow, modulo |
| 3 | Reverse a string in 3 ways | Easy | slicing, two pointers, recursion |

## Prerequisites and follow-ups

- **Before this:** none — start here.
- **Next:** `01-complexity-analysis`, then `02-arrays`.

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
