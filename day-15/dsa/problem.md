# Implement Queue using Stacks

| Field | Value |
|---|---|
| Day | `day-15` |
| Track | `dsa` |
| Topic | `13-queue-and-deque` — see `resources/topics/` |
| Difficulty | Easy |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/implement-queue-using-stacks/ |

## Problem summary

Implement a first-in-first-out queue using only two stacks and the operations
they support (`append`/`pop`, i.e. push and pop at one end). The queue must
support `push(x)`, `pop()`, `peek()`, and `empty()`, with the same answers a
real queue would give — including the case where pushes and pops are
interleaved. The point is not to hide a `deque` behind a class, but to show
that FIFO order can be *reconstructed* from LIFO order by reversing twice.

### Input

- A sequence of valid method calls as described by the platform: at most 100
  calls, `1 <= x <= 9`; `pop`/`peek` are only called on a non-empty queue.

### Output

- `pop()` returns and removes the front element, `peek()` returns the front
  element, `empty()` returns whether the queue holds nothing.

## Approach

1. Keep two stacks: `inbox` (where `push` lands) and `outbox` (where `pop` and
   `peek` read).
2. `push(x)` → `inbox.append(x)`. Nothing else happens.
3. `pop()`/`peek()` first call `_drain_inbox()`: if `outbox` is **empty**,
   pop every element from `inbox` into `outbox`. Reversing the newest-first
   inbox makes the oldest element the top of the outbox.
4. `pop()` → `outbox.pop()`; `peek()` → `outbox[-1]`; `empty()` → both stacks
   empty.
5. The guard `if self._outbox: return` inside `_drain_inbox` is essential:
   draining into a non-empty outbox would put newer elements above older ones
   and break FIFO order.

## Why this approach works

**Invariant (one sentence):** concatenating `outbox` read top-to-bottom with
`inbox` read bottom-to-top always lists the queued elements from oldest to
newest.

*The drain is exactly one reversal.* `inbox` read top-to-bottom is newest to
oldest; popping it into `outbox` reverses that, so the outbox's top is the
oldest element still waiting. Serving only from the outbox therefore always
returns the front of the queue.

*The guard preserves the invariant.* While `outbox` is non-empty it holds a
prefix of the queue in front-to-back order, and all of `inbox` is strictly
newer than everything in it — so appending a drained inbox *under* the current
outbox stack would be correct, but appending it *on top* would not. Skipping
the drain until the outbox empties is the simple way to keep that ordering.

*Amortization is real, not assumed.* Each element is pushed once into `inbox`
and moved at most once into `outbox`; the transfer loop runs once per element
over the queue's lifetime, so the total transfer work across `n` operations is
`O(n)`. That is why `pop`/`peek` are O(1) amortized even though one unlucky
`pop` costs O(n).

## Complexity

- **Time:** `push` O(1) worst case; `pop`/`peek` O(1) amortized (O(n) worst
  case for the single call that drains an inbox of size n); `empty` O(1).
  For any sequence of n operations, total time is O(n) because every element
  crosses at most once.
- **Space:** O(n) — each queued element lives in exactly one of the two stacks,
  so the total number of stored items equals the queue length.

## Edge cases

- Empty queue → `empty()` is `True`; `pop`/`peek` raise `IndexError` (the
  platform never issues those calls, but a class should not silently return a
  wrong value).
- One element → all four operations behave as expected; `peek` does not
  consume, so two peeks in a row agree.
- Pushes after a partial drain (`push 1, push 2, pop, push 3`) → `3` must land
  behind `2`; tested explicitly because it is the case a broken "always drain"
  version gets wrong.
- Duplicate values → FIFO is about positions, not distinct values; `4, 4, 4`
  must still come out in insertion order.
- Alternating push/pop → no transfer ever accumulates, so each operation is
  O(1) worst case, not just amortized.
- Worst-case shape: n pushes then n pops → first pop moves n elements once,
  the remaining n-1 pops are O(1); `moves <= pushes` is asserted to show every
  element crossed at most once.
- Repeated peeks followed by one pop → the outbox is drained once and reused;
  no re-drain on `peek`.
- Only the platform's tiny limits are used in the statement, but the structure
  is O(n) in space for any n and does not depend on recursion.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `push 1, push 2, peek, pop, empty, pop, empty` | `1, 1, False, 2, True` | the statement's example |
| `push 1, push 2, pop, push 3, peek, pop, pop` | `1, 2, 2, 3` | push behind a partially drained queue |
| `push 7, peek, peek, pop` | `7, 7, 7` | peek does not consume |
| `push 5, pop` | `5` | single element |
| `push 4, push 4, push 4` then three pops | `4, 4, 4` | duplicates preserved in order |
| empty `pop`/`peek` | raises `IndexError` | defined empty-queue behaviour |
| 100 pushes then 100 pops, `moves` inspected | first pop moves 100; total moves `<=` pushes | amortized evidence, not a timing |
| 500 random 200-call sequences | agrees with `collections.deque` on every call | randomized differential check |

## What I learned

- **Pattern:** two LIFO stacks compose into FIFO because two reversals cancel.
  This is the smallest concrete example of the more general "simulate one
  structure with another" exercise, and the same two-stack idea evaluates
  expressions and iterates trees without recursion.
- **Pitfall:** the natural first version drains the inbox on *every* pop/peek.
  It still returns correct values on simple tests but destroys the amortized
  bound and breaks order as soon as a push interleaves with a partially full
  outbox — the drain guard is load-bearing, not an optimization.
- **Differently next time:** assert the structural counter (`moves <= pushes`)
  in the tests. Timing would show the same thing but would be machine-dependent
  and flaky; counting the actual transfers proves the bound directly.

**Review date:** 2026-11-22 (1 day) · 2026-11-28 (7 days) · 2026-12-21 (30 days)
