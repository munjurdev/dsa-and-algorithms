# 12 — Stack

> Phase 5 · Roadmap Days 086–090 · Folder: `12-stack/`

Last in, first out: the data structure of *undo*, *matching*, and *the
element I haven't seen its answer for yet*.

## Purpose

Stacks power bracket matching, expression evaluation, and the monotonic-stack
family ("next greater element") that shows up constantly in medium/hard
interviews. The monotonic idea — keeping candidates in sorted order so you
can discard many at once — is a transferable superpower.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| LIFO discipline | push/pop on one end only | implement with `list` (append/pop) |
| Bracket matching | open brackets pushed, closers compared | handle nesting and invalid inputs |
| Expression stacks | operands and operators in two stacks | infix → postfix evaluation |
| Monotonic stack | elements stay increasing/decreasing | next-greater/smaller in `O(n)` |
| Simulated recursion | explicit stack replaces call frames | iterative DFS when depth is large |

## Key patterns

1. **Match on the top** — pop when the current element completes a pair.
2. **Pop while greater/less** — each element is pushed and popped once →
   `O(n)` total.
3. **Stack of pending work** — deferred computation (and/or graphs).

## Complexity expectations

- `O(n)` time for all monotonic-stack problems; `O(n)` space worst case
  (strictly decreasing input).

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | matching with a stack |
| 2 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | monotonic decreasing stack |
| 3 | [Min Stack](https://leetcode.com/problems/min-stack/) | Medium | auxiliary min tracking |

## Prerequisites and follow-ups

- **Before this:** `11-linked-list`, `02-arrays`.
- **Next:** `13-queue-and-deque`, `14-recursion` (the call stack is a stack).

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
