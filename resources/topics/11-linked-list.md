# 11 — Linked List

> Phase 5 · Roadmap: see `ROADMAP.md` · File: `resources/topics/11-linked-list.md`

Nodes and pointers instead of arrays: the structure that forces you to think
about *references*, in-place rewiring, and `O(1)` operations arrays cannot do.

## Purpose

Linked lists are the purest pointer-manipulation practice: reversal,
merging, and cycle detection teach the discipline that trees and graphs
require. Interviews also test them because index-based intuition fails here.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Singly vs doubly linked | forward-only vs bidirectional links | pick based on operation needs |
| Sentinel (dummy) node | avoids head-removal special cases | use it in every list problem |
| Fast/slow pointers | Floyd's tortoise and hare | detect cycles and find middles |
| In-place reversal | flip `node.next` without losing the rest | reverse a list iteratively and recursively |
| Merge of two sorted lists | always take the smaller head | merge in `O(1)` extra space |
| Two passes | reach index n-k by counting first | remove nth node from end |

## Key patterns

1. **Dummy head + `prev` pointer** — uniform handling of insert/delete.
2. **`curr`/`nxt` two-variable reversal** — the classic lost-link bug happens
   when you forget to save `nxt` first.
3. **Split at middle, merge halves** — mergesort / reorder list family.

## Complexity expectations

- Time `O(n)` per traversal; reversing/merging in `O(1)` extra space
  (output list excluded); no random access — `O(n)` to reach index `i`.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | iterative + recursive reversal |
| 2 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | fast/slow pointers |
| 3 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | dummy node, interleaving |

## Prerequisites and follow-ups

- **Before this:** `02-arrays`, `10-binary-search`.
- **Next:** `12-stack`, `13-queue-and-deque`; later `16-trees` (same pointer
  thinking one level deeper).

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
