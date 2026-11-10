"""
Solution for: Product of Array Except Self
Day:      day-09
Track:    algorithms
Difficulty: Medium

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Build the answer in two passes over the output array. The left-to-right
    pass writes the product of everything before each index; the right-to-left
    pass multiplies in the product of everything after it, carrying a single
    running suffix. Division is never used, so zeros need no special case, and
    the only extra storage is the output array itself.

Time Complexity:  O(n)   # two linear passes, constant work per element
Space Complexity: O(1)   # extra space beyond the returned array
"""

from __future__ import annotations

import math
import random


def product_except_self(nums: list[int]) -> list[int]:
    """Return the product of all elements except the one at each index.

    Args:
        nums: array of integers; zeros and negatives are allowed. Must contain
            at least two elements for `Product of Array Except Self`; shorter
            inputs are still handled without error.

    Returns:
        A new list where `result[i] == prod(nums[:i]) * prod(nums[i + 1:])`.
        For a single element the empty product is `1`.
    """
    # --- Solution -------------------------------------------------------
    n = len(nums)
    result = [1] * n

    # product of everything strictly to the left of i
    prefix = 1
    for index in range(n):
        result[index] = prefix
        prefix *= nums[index]

    # multiply in the product of everything strictly to the right of i
    suffix = 1
    for index in range(n - 1, -1, -1):
        result[index] *= suffix
        suffix *= nums[index]

    return result


def _brute_force_product(nums: list[int]) -> list[int]:
    """O(n^2) reference: multiply every other element for each index."""
    return [
        math.prod(value for other, value in enumerate(nums) if other != index)
        for index in range(len(nums))
    ]


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # The statement's example
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    # Degenerate sizes: the empty product is 1
    assert product_except_self([]) == []
    assert product_except_self([5]) == [1]
    assert product_except_self([0]) == [1]

    # Two elements: each answer is the other element
    assert product_except_self([2, 3]) == [3, 2]
    assert product_except_self([0, 7]) == [7, 0]

    # Zeros: one zero makes every other answer zero; two zeros make all zero
    assert product_except_self([0, 0]) == [0, 0]
    assert product_except_self([1, 0]) == [0, 1]
    assert product_except_self([0, 1, 2]) == [2, 0, 0]
    assert product_except_self([0, 1, 0, 2]) == [0, 0, 0, 0]
    assert product_except_self([0, 0, 5]) == [0, 0, 0]

    # Negatives: signs must follow the count of negatives left behind
    assert product_except_self([-1, -2, -3, -4]) == [-24, -12, -8, -6]
    assert product_except_self([1, -1]) == [-1, 1]
    assert product_except_self([-2, 0, -3]) == [0, 6, 0]

    # Repeated values and a longer array
    assert product_except_self([2, 2, 2]) == [4, 4, 4]
    assert product_except_self([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]

    # A zero in a long array: only the zero's own slot survives
    assert product_except_self([1, 2, 0, 4, 5]) == [0, 0, 40, 0, 0]

    # The caller's list is never mutated
    nums = [1, 2, 3, 4]
    assert product_except_self(nums) == [24, 12, 8, 6]
    assert nums == [1, 2, 3, 4]

    # Exhaustive differential check on tiny arrays against the brute force
    for size in range(0, 6):
        for values in _tuples_of(range(-2, 3), size):
            nums = list(values)
            assert product_except_self(nums) == _brute_force_product(nums), nums

    # Randomized check on larger arrays, zeros and negatives included
    rng = random.Random(20261110)
    for _ in range(400):
        size = rng.randint(0, 20)
        nums = [rng.randint(-4, 4) for _ in range(size)]
        assert product_except_self(nums) == _brute_force_product(nums), nums

    print("All tests passed.")


def _tuples_of(values: range, size: int):
    """Yield every `size`-tuple drawn from `values` (order matters)."""
    if size == 0:
        yield ()
        return
    for head in values:
        for tail in _tuples_of(values, size - 1):
            yield (head, *tail)


if __name__ == "__main__":
    main()
