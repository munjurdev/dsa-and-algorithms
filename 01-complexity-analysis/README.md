# 01 — Complexity Analysis

> Phase 1 · Roadmap Days 010–015 · Folder: `01-complexity-analysis/`

Learn to state *why* a solution is fast or slow before writing it — the
analysis is what interviewers grade, not just the code.

## Purpose

Big-O gives you a common language for trade-offs and a shortcut for choosing
algorithms: the constraint table on a problem tells you which complexities are
even allowed.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Asymptotic growth | Behavior as `n → ∞`, constants dropped | classify any loop nest in seconds |
| Best / average / worst | Different inputs can cost different amounts | state which one you mean |
| Amortized analysis | Occasional expensive ops averaged out | justify `list.append` as `O(1)` |
| Space complexity | Auxiliary memory, including recursion stack | spot hidden `O(n)` in memo tables |
| Master theorem | Cost of `T(n) = a·T(n/b) + f(n)` | derive merge sort's `O(n log n)` |

## Key patterns

1. **Constraints first** — read `n`, derive the allowed complexity, then
   design.
2. **Count the work inside the innermost statement**, not the number of loops.
3. **Name the invariant** — "each element enters and leaves the window once"
   is an `O(n)` proof.

## Complexity expectations

- Master: recognize `O(1)`, `O(log n)`, `O(n)`, `O(n log n)`, `O(n^2)`,
  `O(2^n)` on sight.
- Be able to convert an `O(n^2)` idea into `O(n log n)` or `O(n)` by naming
  the wasted work.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | Analyze 10 given code snippets | Easy | loop counting, no coding |
| 2 | Two-sum: `O(n^2)` vs `O(n)` | Easy | trading space for time |
| 3 | Count operations for n = 10⁶ | Medium | rough runtime estimation |

## Prerequisites and follow-ups

- **Before this:** `00-python-fundamentals`.
- **Next:** `02-arrays` — apply the analysis to real problems.

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Reference: `notes/complexity-cheatsheet.md`.
