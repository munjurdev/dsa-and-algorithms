# Linked List Cycle

| Field | Value |
|---|---|
| Day | `day-13` |
| Track | `algorithms` |
| Topic | `11-linked-list` (Floyd's tortoise and hare) — see `resources/topics/` |
| Difficulty | Easy |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/linked-list-cycle/ |

## Problem summary

Decide whether following `next` from the head of a singly linked list ever
revisits a node. A list with a cycle has no end, so any loop that walks it
naively hangs — the answer must be reached without marking nodes, in `O(1)`
extra space. Two pointers at different speeds settle it: on an acyclic list the
fast one runs off the end, and on a cyclic one it must eventually catch the slow
one.

### Input

- `head: ListNode | None` — first node of a list with `0 <= len <= 10⁴`, values
  in `-10⁵..10⁵`; a cycle, if present, starts at some node and points back into
  the list.
- The structure is given, not its cycle position — `pos` exists only in the
  platform's examples, not as an argument.

### Output

- `bool` — `True` if the list contains a cycle, `False` otherwise (an empty
  list is acyclic by definition).

## Approach

1. Start both pointers at `head`: `slow` and `fast`.
2. While `fast` and `fast.next` both exist:
   - `slow = slow.next` (one node per step);
   - `fast = fast.next.next` (two nodes per step);
   - if `slow is fast`, a cycle exists → `True`.
3. If the loop ends, `fast` fell off the end, so the list is finite → `False`.

The comparison is by **identity**, not value: two different nodes with the same
`val` are not a cycle.

## Why this approach works

**Invariant (one sentence):** `slow` and `fast` both start at the head and
`fast` moves exactly twice as far, so `fast` is always `d` nodes further along
the cycle than `slow` — and that distance shrinks by one per iteration while
both are inside the cycle.

*Acyclic lists terminate.* Every iteration moves `fast` two nodes closer to the
end; `fast is None` or `fast.next is None` signals the end, and the guard tests
exactly the two nodes the double step would dereference, so no `AttributeError`
can occur.

*Cyclic lists are detected.* Once `slow` enters the cycle (at most `n` steps),
`fast` is already inside it. Both then loop forever, and because the gap
between them decreases by one node per step modulo the cycle length `L`, it
reaches `0` within `L` steps — at which point `slow is fast`. Detection
therefore happens within `n + L <= 2n` iterations, never later.

*Constant space.* The two pointers are the entire state; no node is marked, and
the list is not mutated, so the original structure is preserved for the caller.

## Complexity

- **Time:** O(n) — the fast pointer advances two nodes per iteration and enters
  the cycle within `n` steps; the gap then closes in at most `L <= n` more
  iterations, so `O(n)` total with constant work per step.
- **Space:** O(1) — two pointers, no visited set, no recursion, no mutation.

## Edge cases

- `head is None` → the loop does not run → `False`.
- Single node with `next = None` → `False`; single node pointing at itself →
  `True` (guard passes, `slow is fast` after one step).
- Two nodes forming a cycle (`[1,2]` with `2 -> 1`) → `True` on the first
  iteration.
- Tail pointing back to the head (`pos = 0`) → `True`; tail self-loop
  (`pos = len - 1`) → `True` (the two-pointer catch-up still happens inside a
  length-1 cycle).
- Long acyclic list (1000 nodes) → `False` without touching a null node's
  fields.
- Duplicate values without a cycle → `False`; identity comparison is what makes
  this correct, and a `val`-based check would report a false positive.
- A cycle that starts after a long acyclic prefix → handled without a special
  case; the pointers simply meet later.
- `pos` is not an argument — the helper `build_with_cycle` exists only for tests
  and rejects `pos >= len`.
- The input list is never modified, so a caller can still use it afterwards.
- Platform maximum (`10⁴` nodes) is traversed once by `fast`.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[3,2,0,-4]`, tail → index 1 | `True` | the statement's example |
| `[1,2]`, tail → index 0 | `True` | two-node cycle |
| `[1]`, no cycle | `False` | single node, no cycle |
| `[]` | `False` | empty list |
| `[1,2,3]`, no cycle | `False` | acyclic short list |
| `[1,2,3]`, tail self-loop | `True` | cycle of length 1 |
| `[1]`, `pos = 0` | `True` | node points at itself |
| `[1,2,3,4]`, tail → head | `True` | whole list is the cycle |
| `[1,2,3,4]`, tail → tail | `True` | self-loop at the end |
| `range(1000)`, no cycle | `False` | long acyclic list, guard must stop cleanly |
| `range(1000)`, tail self-loop | `True` | long prefix, tiny cycle |
| every size `0..8` with every `pos` in `-1..size-1` | `pos >= 0` | exhaustive check |
| 500 random lists (size 0–40, random entry point) | equals the visited-set oracle | randomized differential check |

## What I learned

- **Pattern:** two pointers at different speeds convert "does this loop?" into
  "do these two ever collide?" — the same catch-up argument later powers finding
  the middle of a list and the entry node of the cycle.
- **Pitfall:** comparing `slow.val == fast.val` instead of `slow is fast` looks
  equivalent on the platform's examples but is wrong for lists with duplicate
  values; and checking only `fast is not None` before `fast.next.next` segfaults
  on a one-node tail. Both guards are required.
- **Differently next time:** build the test helper first (`build_with_cycle`)
  and make the naive visited-set oracle part of the tests — a cycle detector
  that hangs is a silent failure, and the oracle makes "wrong answer" and
  "infinite loop" distinguishable.

**Review date:** 2026-11-19 (1 day) · 2026-11-25 (7 days) · 2026-12-18 (30 days)
