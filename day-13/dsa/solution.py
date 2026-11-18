"""
Solution for: Reverse Linked List
Day:      day-13
Track:    dsa
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Iterative: walk the list once, saving `curr.next` before overwriting it,
    then point `curr.next` backwards at `prev` and advance both pointers. When
    `curr` falls off the end, `prev` is the old tail and therefore the new head.
    Recursive: reverse everything after the head, then let the next node point
    back at the head and cut the head's own link; the recursion's returned node
    is always the new head. Both are O(n); the iterative one uses O(1) space and
    the recursive one uses O(n) call frames.

Time Complexity:  O(n)  # each node visited once, constant work per node
Space Complexity: O(1)  # iterative: three pointers; recursive variant is O(n) stack

Review Date:  2026-11-19 (1 day) · 2026-11-25 (7 days) · 2026-12-18 (30 days)
"""

from __future__ import annotations

import random
import sys


class ListNode:
    """A singly linked list node (the platform's definition)."""

    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse the list in place, iteratively, and return the new head.

    Args:
        head: the first node, or ``None`` for an empty list.

    Returns:
        The old tail (new head), or ``None`` when the list was empty. No node is
        created or destroyed — only ``next`` links change.
    """
    # --- Solution -------------------------------------------------------
    prev: ListNode | None = None
    curr = head

    while curr is not None:
        nxt = curr.next  # save the rest before breaking the link
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def reverse_list_recursive(head: ListNode | None) -> ListNode | None:
    """Reverse the list recursively and return the new head.

    Args:
        head: the first node, or ``None`` for an empty list.

    Returns:
        The old tail (new head), or ``None`` when the list was empty.

    Note:
        Uses one call frame per node, so it needs ``len(list) + 1`` frames and
        hits Python's default recursion limit around 1000 nodes. The platform
        allows 5000, which is why the iterative version is the primary answer.
    """
    if head is None or head.next is None:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head  # the next node now points back at us
    head.next = None  # and we become the new tail
    return new_head


def build(values: list[int]) -> ListNode | None:
    """Build a list from `values` and return its head."""
    head: ListNode | None = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_list(head: ListNode | None) -> list[int]:
    """Collect the node values in order. Raises on a cycle instead of hanging."""
    values: list[int] = []
    seen: set[int] = set()
    node = head
    while node is not None:
        node_id = id(node)
        if node_id in seen:
            raise AssertionError("cycle in a list that should be acyclic")
        seen.add(node_id)
        values.append(node.val)
        node = node.next
    return values


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # Typical case: 1 -> 2 -> 3 -> 4 -> 5 becomes 5 -> 4 -> 3 -> 2 -> 1
    assert to_list(reverse_list(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse_list_recursive(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]

    # Edge cases: empty list, single node, two nodes
    assert reverse_list(None) is None
    assert reverse_list_recursive(None) is None
    assert to_list(reverse_list(build([7]))) == [7]
    assert to_list(reverse_list_recursive(build([7]))) == [7]
    assert to_list(reverse_list(build([1, 2]))) == [2, 1]
    assert to_list(reverse_list_recursive(build([1, 2]))) == [2, 1]

    # Duplicates and negatives survive unchanged in order
    assert to_list(reverse_list(build([-1, 0, 0, 3, -1]))) == [-1, 3, 0, 0, -1]

    # Both variants agree with the list's own reversal, for sizes 0..8
    for size in range(9):
        values = list(range(size))
        assert to_list(reverse_list(build(values))) == values[::-1]
        assert to_list(reverse_list_recursive(build(values))) == values[::-1]

    # In place: no node is allocated and the old tail is the returned node
    head = build([1, 2, 3])
    old_tail = head.next.next
    new_head = reverse_list(head)
    assert new_head is old_tail
    assert head.next is None  # the old head is now the tail

    # Randomized check across both variants
    rng = random.Random(20261118)
    for _ in range(200):
        size = rng.randint(0, 50)
        values = [rng.randint(-100, 100) for _ in range(size)]
        expected = values[::-1]
        assert to_list(reverse_list(build(values))) == expected
        if size + 2 < sys.getrecursionlimit():
            assert to_list(reverse_list_recursive(build(values))) == expected

    print("All tests passed.")


if __name__ == "__main__":
    main()
