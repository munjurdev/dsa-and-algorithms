"""
Solution for: Linked List Cycle
Day:      day-13
Track:    algorithms
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Run two pointers from the head at different speeds — `slow` advances one
    node per step, `fast` advances two. If the list ends (`fast` or
    `fast.next` becomes None) there is no cycle. If there is one, both pointers
    eventually enter it, and inside the loop the fast pointer closes the gap to
    the slow one by exactly one node per step, so it must land on it within one
    loop length. No node is ever marked, which is what keeps the space constant.

Time Complexity:  O(n)  # the fast pointer traverses each node at most once before meeting or ending
Space Complexity: O(1)  # two pointers; no visited set

Review Date:  2026-11-19 (1 day) · 2026-11-25 (7 days) · 2026-12-18 (30 days)
"""

from __future__ import annotations

import random


class ListNode:
    """A singly linked list node (the platform's definition)."""

    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    """Return True iff following `next` from `head` ever revisits a node.

    Args:
        head: the first node, or ``None`` for an empty list.

    Returns:
        ``True`` if the list contains a cycle, ``False`` for an acyclic list
        (including the empty one).
    """
    # --- Solution -------------------------------------------------------
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


def build_with_cycle(values: list[int], pos: int) -> ListNode | None:
    """Build a list from `values`, linking the tail to index `pos` if >= 0."""
    if not values:
        return None

    nodes = [ListNode(value) for value in values]
    for current, following in zip(nodes, nodes[1:]):
        current.next = following

    if pos >= 0:
        if pos >= len(nodes):
            raise ValueError("pos must be -1 or a valid index")
        nodes[-1].next = nodes[pos]

    return nodes[0]


def _has_cycle_visited(head: ListNode | None) -> bool:
    """O(n) space reference: a node is revisited iff there is a cycle."""
    seen: set[int] = set()
    node = head
    while node is not None:
        if id(node) in seen:
            return True
        seen.add(id(node))
        node = node.next
    return False


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's examples
    assert has_cycle(build_with_cycle([3, 2, 0, -4], 1)) is True
    assert has_cycle(build_with_cycle([1, 2], 0)) is True
    assert has_cycle(build_with_cycle([1], -1)) is False

    # Edge cases: empty list, single node, cycle back to the head, tail cycle
    assert has_cycle(None) is False
    assert has_cycle(build_with_cycle([], -1)) is False
    assert has_cycle(build_with_cycle([1, 2, 3], -1)) is False
    assert has_cycle(build_with_cycle([1, 2, 3], 2)) is True  # self-loop on the tail
    assert has_cycle(build_with_cycle([1], 0)) is True  # node points at itself
    assert has_cycle(build_with_cycle([1, 2, 3, 4], 0)) is True  # tail -> head
    assert has_cycle(build_with_cycle([1, 2, 3, 4], 3)) is True  # tail -> tail

    # Long acyclic list: the fast pointer must stop at the end, not crash
    assert has_cycle(build_with_cycle(list(range(1000)), -1)) is False
    assert has_cycle(build_with_cycle(list(range(1000)), 999)) is True

    # Exhaustive check over every size and every entry point
    for size in range(0, 9):
        values = list(range(size))
        for pos in range(-1, size):
            got = has_cycle(build_with_cycle(values, pos))
            want = pos >= 0
            assert got is want, (size, pos, got, want)

    # Randomized differential check against the visited-set oracle
    rng = random.Random(20261118)
    for _ in range(500):
        size = rng.randint(0, 40)
        values = [rng.randint(-100, 100) for _ in range(size)]
        pos = rng.randint(-1, size - 1) if size else -1
        head = build_with_cycle(values, pos)
        got = has_cycle(head)
        want = _has_cycle_visited(head)
        assert got is want, (size, pos, got, want)

    print("All tests passed.")


if __name__ == "__main__":
    main()
