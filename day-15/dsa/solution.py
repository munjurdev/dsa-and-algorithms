"""
Solution for: Implement Queue using Stacks
Day:      day-15
Track:    dsa
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Keep two stacks: `inbox` receives every push, `outbox` serves every pop and
    peek. When `outbox` is empty, reverse `inbox` into it one element at a
    time, which puts the oldest element on top. Since an element is transferred
    at most once in its lifetime, push is O(1) worst case and pop/peek are O(1)
    amortized (a single pop can still cost O(n) when it triggers a transfer).

Time Complexity:  O(1) amortized per operation; O(n) worst case for one pop/peek that drains the inbox
Space Complexity: O(n)  # the two stacks together hold every queued element once

Review Date:  2026-11-22 (1 day) · 2026-11-28 (7 days) · 2026-12-21 (30 days)
"""

from __future__ import annotations

import random
from collections import deque


class MyQueue:
    """FIFO queue built only from two LIFO stacks.

    `moves` counts element transfers between the stacks. It is test
    instrumentation, not part of the LeetCode interface: the amortized bound
    is only credible if every element crosses at most once, and that is a
    property a test can assert.
    """

    def __init__(self) -> None:
        self._inbox: list[int] = []
        self._outbox: list[int] = []
        self.moves = 0

    def push(self, x: int) -> None:
        """Append `x` at the back of the queue."""
        self._inbox.append(x)

    def pop(self) -> int:
        """Remove and return the front element.

        Raises:
            IndexError: if the queue is empty (LeetCode never calls it).
        """
        self._drain_inbox()
        if not self._outbox:
            raise IndexError("pop from an empty queue")
        return self._outbox.pop()

    def peek(self) -> int:
        """Return the front element without removing it.

        Raises:
            IndexError: if the queue is empty (LeetCode never calls it).
        """
        self._drain_inbox()
        if not self._outbox:
            raise IndexError("peek from an empty queue")
        return self._outbox[-1]

    def empty(self) -> bool:
        """Return True iff no element is waiting."""
        return not self._inbox and not self._outbox

    def _drain_inbox(self) -> None:
        """Move the inbox into the outbox, but only when the outbox is empty.

        The condition is what makes the bound amortized: draining while the
        outbox still holds elements would destroy the FIFO order.
        """
        if self._outbox:
            return
        while self._inbox:
            self._outbox.append(self._inbox.pop())
            self.moves += 1


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # --- Statement example ----------------------------------------------
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() is False
    assert queue.pop() == 2
    assert queue.empty() is True

    # --- Interleaved: a push after a drain queues behind what is left ----
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.pop() == 1
    queue.push(3)
    assert queue.peek() == 2
    assert queue.pop() == 2
    assert queue.pop() == 3
    assert queue.empty() is True

    # --- peek must not consume; two peeks in a row agree ------------------
    queue = MyQueue()
    queue.push(7)
    assert queue.peek() == 7
    assert queue.peek() == 7
    assert queue.pop() == 7
    assert queue.empty() is True

    # --- Single element, duplicate values ---------------------------------
    queue = MyQueue()
    queue.push(5)
    assert queue.pop() == 5
    queue = MyQueue()
    for value in (4, 4, 4):
        queue.push(value)
    assert [queue.pop() for _ in range(3)] == [4, 4, 4]

    # --- Invalid access on an empty queue ---------------------------------
    for operation in (MyQueue().pop, MyQueue().peek):
        try:
            operation()
        except IndexError:
            pass
        else:  # pragma: no cover - only runs if the guard is missing
            raise AssertionError("empty queue access must raise IndexError")

    # --- Amortized evidence: n elements cross the stacks at most once -----
    queue = MyQueue()
    for value in range(100):
        queue.push(value)
    assert queue.moves == 0  # pushes never touch the second stack
    assert queue.pop() == 0
    assert queue.moves == 100  # the one expensive pop moved everything
    assert queue.pop() == 1
    assert queue.moves == 100  # every later pop is O(1)
    assert queue.empty() is False

    # --- Randomized differential check against collections.deque ----------
    rng = random.Random(20261121)
    for _ in range(500):
        queue = MyQueue()
        reference: deque[int] = deque()
        next_value = 1
        pushes = 0

        for _ in range(200):
            action = rng.choice(("push", "push", "pop", "peek", "empty"))
            if action == "push":
                queue.push(next_value)
                reference.append(next_value)
                next_value += 1
                pushes += 1
            elif not reference:
                assert queue.empty() is True
            elif action == "pop":
                assert queue.pop() == reference.popleft()
            elif action == "peek":
                assert queue.peek() == reference[0]
            else:
                assert queue.empty() is (not reference)

        while reference:
            assert queue.pop() == reference.popleft()
        assert queue.empty() is True
        assert queue.moves <= pushes

    print("All tests passed.")


if __name__ == "__main__":
    main()
