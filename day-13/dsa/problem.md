# Reverse Linked List

| Field | Value |
|---|---|
| Day | `day-13` |
| Track | `dsa` |
| Topic | `11-linked-list` — see `resources/topics/` |
| Difficulty | Easy |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/reverse-linked-list/ |

## Problem summary

Given the head of a singly linked list, reverse the direction of every `next`
pointer and return the new head (the old tail). The nodes themselves are not
copied or replaced — only the links move, which is why this is the canonical
first pointer-rewiring exercise. Both an iterative and a recursive solution are
expected; the iterative one is the answer that survives the platform's
5000-node limit.

### Input

- `head: ListNode | None` — the first node of a list with
  `0 <= len <= 5000`, values in `-5000..5000` (duplicates allowed); may be
  `None`.

### Output

- `ListNode | None` — the head of the same nodes in reverse order; `None` for
  an empty list.

## Approach

**Iterative** (primary):

1. `prev = None`, `curr = head`.
2. While `curr` is not `None`:
   - save `nxt = curr.next` **before** touching the link;
   - set `curr.next = prev` (turn the node around);
   - advance `prev = curr`, `curr = nxt`.
3. Return `prev` — after the loop it is the node that used to be the tail.

**Recursive**:

1. Base case: an empty list or a single node is already reversed — return it.
2. Recurse on `head.next`; the returned node is the new head (the old tail).
3. Now `head.next` is the last node of the reversed tail, so set
   `head.next.next = head` and `head.next = None` to append `head` at the end.
4. Return the new head unchanged.

## Why this approach works

**Invariant (one sentence), iterative:** at the top of each iteration, `prev` is
the head of the reversed prefix and `curr` is the head of the untouched suffix,
with the two joined by `prev`'s final `next` having been reset and `curr`'s link
still pointing into the suffix.

*Nothing is lost.* `nxt` is saved before `curr.next` is overwritten, so the
unprocessed tail remains reachable at every step — the classic lost-link bug is
avoided by ordering, not by luck.

*Every edge is flipped exactly once.* The loop visits each node once and sets
its `next` to its predecessor. The old head ends with `next = None` (it starts
as `prev = None` for the first iteration), so the new list is properly
terminated, and the old tail is returned as the head.

**Invariant, recursive:** the recursive call returns the reversed version of
`head.next`'s list, whose tail is `head.next`. Appending `head` there and
clearing `head.next` yields the reversed version of the whole list, so the
induction closes at the base case.

## Complexity

- **Time:** O(n) — one visit per node, constant pointer work; the recursive
  version also does constant work per frame.
- **Space:** O(1) iterative (three pointers) versus O(n) for the recursion
  stack; the platform allows 5000 nodes, so the recursive version needs
  `sys.setrecursionlimit` beyond ~1000 and is documented as the secondary form.

## Edge cases

- `head is None` → `None` from both variants.
- Single node → returned unchanged, `next` already `None`.
- Two nodes → `[1, 2]` becomes `[2, 1]`; both branches of the loop body run.
- All values equal → reversal is structurally visible but not value-visible;
  tests check node identity/in-place behaviour, not just values.
- Negative and duplicate values → carried through untouched.
- In-place guarantee: the returned head **is** the old tail node
  (`assert new_head is old_tail`) and the old head's `next` is `None` — no new
  nodes are allocated.
- Recursion depth: 5000 nodes exceeds Python's default limit of 1000, so the
  iterative version is the one used for full-size input; the recursive version
  is verified on smaller sizes and stated as O(n) space.
- Reversing an already-reversed list restores the original — not tested as a
  separate case because it is two applications of the same invariant.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `[1,2,3,4,5]` | `[5,4,3,2,1]` | the statement's example, both variants |
| `[]` | `[]` | empty list, both variants |
| `[7]` | `[7]` | single node |
| `[1,2]` | `[2,1]` | minimum case where a link actually flips |
| `[-1,0,0,3,-1]` | `[-1,3,0,0,-1]` | negatives and duplicates |
| every `list(range(n))` for `n = 0..8` | `values[::-1]` | small exhaustive check, both variants |
| `[1,2,3]` node identity | new head is the old tail; old head's `next` is `None` | proves the reversal is in place |
| 200 random lists (size 0–50, values `-100..100`) | `values[::-1]` | randomized check, both variants |

## What I learned

- **Pattern:** pointer rewiring needs an explicit "reversed prefix / untouched
  suffix" invariant; once written down, the three-pointer loop is mechanical,
  and the recursive form is the same statement read backwards.
- **Pitfall:** `curr.next = prev` before saving `curr.next` truncates the list
  and leaves `curr` unreachable — the test that catches it is not a value
  comparison but the random-size loop, because a truncated list often still
  produces a plausible-looking short output.
- **Differently next time:** state whether the function must be in place before
  coding. It decides between allocating a new list (easy, but wrong for the
  interview) and rewiring, and it decides which assertions (node identity, not
  just values) belong in `main()`.

**Review date:** 2026-11-19 (1 day) · 2026-11-25 (7 days) · 2026-12-18 (30 days)
