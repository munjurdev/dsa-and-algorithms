"""
Solution for: Koko Eating Bananas
Day:      day-12
Track:    algorithms
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Do not simulate one speed at a time — binary search the speed itself. The
    predicate "can finish at speed v?" is monotone: if v is fast enough then
    every speed above it is too, so the set of feasible speeds is a suffix of
    1..max(piles). Binary search its first element. Each test costs one pass
    over the piles summing ceil(pile / v), which makes the whole thing
    O(n log max(piles)).

Time Complexity:  O(n log m)  # m = max(piles); one O(n) feasibility pass per halving
Space Complexity: O(1)        # two bounds and a running hour total

Review Date:  2026-11-19 (1 day) · 2026-11-25 (7 days) · 2026-12-18 (30 days)
"""

from __future__ import annotations

import random


def min_eating_speed(piles: list[int], h: int) -> int:
    """Return the slowest speed that clears every pile within `h` hours.

    Args:
        piles: bananas per pile, each pile eaten from one pile per hour.
        h: hours available, including partial hours of a pile.

    Returns:
        The smallest integer speed (bananas per hour) that finishes in time,
        or `0` when there is nothing to eat.

    Raises:
        ValueError: if `h` is smaller than the number of piles (impossible: one
            pile always costs at least one hour) or negative.
    """
    # --- Solution -------------------------------------------------------
    if not piles:
        return 0
    if h < len(piles):
        raise ValueError("h is too small to eat every pile")

    def hours_needed(speed: int) -> int:
        """Hours to clear all piles at `speed` (ceil per pile, no leftover carry)."""
        return sum((pile + speed - 1) // speed for pile in piles)

    lo, hi = 1, max(piles)  # feasible(hi) is always true; feasible(lo) may not be

    while lo < hi:
        mid = (lo + hi) // 2
        if hours_needed(mid) <= h:
            hi = mid  # feasible, but something slower might be too
        else:
            lo = mid + 1  # too slow, the answer is strictly larger

    return lo


def _linear_scan(piles: list[int], h: int) -> int:
    """O(n · max(piles)) reference: the first speed that fits, or -1."""
    if not piles:
        return 0
    if h < len(piles):
        return -1
    for speed in range(1, max(piles) + 1):
        total = 0
        for pile in piles:
            total += -(-pile // speed)  # ceiling division
        if total <= h:
            return speed
    return -1


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's examples
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23

    # Edge cases: nothing to eat, one pile, the tightest possible hour budget
    assert min_eating_speed([], 5) == 0
    assert min_eating_speed([7], 1) == 7
    assert min_eating_speed([7], 100) == 1
    assert min_eating_speed([1, 1, 1, 1], 4) == 1
    assert min_eating_speed([312884470], 312884469) == 2

    # h == len(piles): each pile must be finished in a single hour
    assert min_eating_speed([3, 6, 7, 11], 4) == 11
    assert min_eating_speed([805306368, 805306368, 805306368], 3) == 805306368

    # Large h collapses the answer to 1 hour per pile
    assert min_eating_speed([1000000000], 1000000000) == 1
    assert min_eating_speed([1000000000], 2) == 500000000
    assert min_eating_speed([805306368, 805306368, 805306368], 1000000000) == 3

    # Impossible budgets are rejected instead of silently returning "no answer"
    for bad_h in (0, 1, 2):
        try:
            min_eating_speed([3, 6, 7], bad_h)
        except ValueError:
            pass
        else:
            raise AssertionError(f"expected ValueError for h={bad_h}")

    # Exhaustive differential check on small inputs
    for size in range(1, 4):
        for _ in range(40):
            piles = [random.Random(size * 100 + _).randint(1, 9) for _ in range(size)]
            for h in range(size, 4 * size + 2):
                got = min_eating_speed(piles, h)
                want = _linear_scan(piles, h)
                assert got == want, (piles, h, got, want)

    # Randomized differential check with larger piles and budgets
    rng = random.Random(20261118)
    for _ in range(300):
        size = rng.randint(1, 20)
        piles = [rng.randint(1, 500) for _ in range(size)]
        h = rng.randint(size, size + 200)
        got = min_eating_speed(piles, h)
        want = _linear_scan(piles, h)
        assert got == want, (piles, h, got, want)

    print("All tests passed.")


if __name__ == "__main__":
    main()
