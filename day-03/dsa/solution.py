"""
Solution for: Constraint range → allowed complexity mapping
Day:      day-03
Track:    dsa
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Each candidate complexity is written as an operation-count formula in n
    (O(1) is 1, O(n log n) is n*log2(n), and 2^n / n! return inf once n is
    large enough that computing them is pointless). `allowed_complexities(n)`
    evaluates all eight formulas at n and keeps the labels whose count fits a
    10^8-operation budget; `allowed_for_range(lo, hi)` delegates with hi,
    because every formula is non-decreasing so the largest n is the binding
    constraint.

Time Complexity:  O(1)   # eight formula evaluations, each O(1)
Space Complexity: O(1)   # the returned list holds at most the 8 labels

Review Date:  2026-11-03 / 2026-11-09 / 2026-12-02
"""

from __future__ import annotations

import math
from collections.abc import Callable

BUDGET: int = 10 ** 8  # ~1 second of simple operations


def _constant(n: int) -> float:
    """O(1) — no dependence on n."""
    return 1.0


def _logarithmic(n: int) -> float:
    """O(log n) — number of halvings."""
    return math.log2(n) if n > 1 else 0.0


def _linear(n: int) -> float:
    """O(n) — one pass."""
    return float(n)


def _linearithmic(n: int) -> float:
    """O(n log n) — one pass per halving level."""
    return n * math.log2(n) if n > 1 else 0.0


def _quadratic(n: int) -> float:
    """O(n^2) — every ordered pair."""
    return float(n) ** 2


def _cubic(n: int) -> float:
    """O(n^3) — every ordered triple."""
    return float(n) ** 3


def _exponential(n: int) -> float:
    """O(2^n) — guarded: past n = 60 it is far beyond any budget."""
    return math.inf if n > 60 else float(2 ** n)


def _factorial(n: int) -> float:
    """O(n!) — guarded: past n = 20 it is far beyond any budget."""
    return math.inf if n > 20 else float(math.factorial(n))


GROWTH: tuple[tuple[str, Callable[[int], float]], ...] = (
    ("O(1)", _constant),
    ("O(log n)", _logarithmic),
    ("O(n)", _linear),
    ("O(n log n)", _linearithmic),
    ("O(n^2)", _quadratic),
    ("O(n^3)", _cubic),
    ("O(2^n)", _exponential),
    ("O(n!)", _factorial),
)


def allowed_complexities(n: int) -> list[str]:
    """Return the complexities whose operation count fits `BUDGET` at size `n`.

    Args:
        n: the problem's maximum input size; must be >= 1.

    Returns:
        Allowed labels in canonical growth order (fastest first).

    Raises:
        ValueError: if `n` is less than 1.
    """
    if n < 1:
        raise ValueError(f"n must be >= 1, got {n}")
    return [label for label, cost in GROWTH if cost(n) <= BUDGET]


def allowed_for_range(lo: int, hi: int) -> list[str]:
    """Return the complexities allowed for every size in `[lo, hi]`.

    Args:
        lo: smallest input size in the range; must be >= 1.
        hi: largest input size; must be >= `lo`.

    Returns:
        The labels allowed at `hi` — every cost is non-decreasing in n.

    Raises:
        ValueError: if the range is invalid (`lo < 1` or `hi < lo`).
    """
    if lo < 1:
        raise ValueError(f"lo must be >= 1, got {lo}")
    if hi < lo:
        raise ValueError(f"hi must be >= lo, got hi={hi} < lo={lo}")
    return allowed_complexities(hi)


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # Typical case: small n allows everything
    assert allowed_complexities(10) == [label for label, _ in GROWTH]
    assert allowed_complexities(1) == [label for label, _ in GROWTH]

    # Constraint ranges from the mapping table
    assert allowed_complexities(100) == [
        "O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)", "O(n^3)"
    ]
    assert allowed_complexities(10_000) == [
        "O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)"
    ]
    assert allowed_complexities(100_000) == [
        "O(1)", "O(log n)", "O(n)", "O(n log n)"
    ]
    assert allowed_complexities(10_000_000) == ["O(1)", "O(log n)", "O(n)"]
    assert allowed_complexities(10 ** 9) == ["O(1)", "O(log n)"]
    assert allowed_complexities(10 ** 18) == ["O(1)", "O(log n)"]  # no overflow

    # Exact boundaries
    assert "O(n^3)" in allowed_complexities(464)   # 464^3 = 99,897,344
    assert "O(n^3)" not in allowed_complexities(465)
    assert "O(n)" in allowed_complexities(10 ** 8)
    assert "O(n)" not in allowed_complexities(10 ** 8 + 1)

    # Ranges are bounded by their largest size
    assert allowed_for_range(1, 100_000) == allowed_complexities(100_000)
    assert allowed_for_range(50, 50) == allowed_complexities(50)

    # Monotone: a bigger n can only allow a subset of what a smaller n allows
    sizes = [1, 5, 100, 10_000, 10 ** 6, 10 ** 9]
    for smaller, bigger in zip(sizes, sizes[1:]):
        assert set(allowed_complexities(bigger)) <= set(allowed_complexities(smaller))

    # Edge cases: invalid input
    for bad in (0, -7):
        try:
            allowed_complexities(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"allowed_complexities({bad}) should raise")
    try:
        allowed_for_range(10, 5)
    except ValueError:
        pass
    else:
        raise AssertionError("inverted range should raise")

    print("All tests passed.")


if __name__ == "__main__":
    main()
