"""
Checkpoint for: Weekly checkpoint 02 — three closed-notes re-solves + a cost drill
Day:      day-14
Track:    algorithms
Difficulty: Medium

Full write-up (what was re-solved, approach, edge cases, tests, review date)
lives in `problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Three problems from Days 08-13 are rebuilt from blank, one per pattern
    family: Container With Most Water (converging two pointers, Day 08),
    Find All Anagrams in a String (fixed-width sliding window, Day 11), and
    Search in Rotated Sorted Array (binary search on a rotated array, Day 12).
    Each is checked against an independent oracle rather than the remembered
    example. The fourth deliverable is the cost argument for `list.pop(0)`:
    removing index 0 shifts every remaining element down one slot, so it is
    O(n), which makes a queue built on `pop(0)` O(n^2) overall.

Time Complexity:  O(n) per re-solved problem; O(n^2) for an n-step queue built on list.pop(0)
Space Complexity: O(n) for the anagram window; O(1) for the other two

Review Date:  2026-11-20 (1 day) · 2026-11-26 (7 days) · 2026-12-19 (30 days)
"""

from __future__ import annotations

import random
import time
from collections import Counter, deque


# --- Re-solve 1 (Day 08): Container With Most Water ----------------------
def max_area(heights: list[int]) -> int:
    """Return the largest rectangle area between two vertical lines.

    Move the shorter line inward: the width can only shrink, so keeping the
    shorter side can never improve the area.
    """
    left, right = 0, len(heights) - 1
    best = 0

    while left < right:
        height = min(heights[left], heights[right])
        best = max(best, height * (right - left))
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1

    return best


# --- Re-solve 2 (Day 11): Find All Anagrams in a String ------------------
def find_anagrams(s: str, p: str) -> list[int]:
    """Return every start index where an anagram of `p` begins in `s`."""
    width = len(p)
    if width > len(s):
        return []

    need = Counter(p)
    window = Counter(s[:width])
    result = [0] if window == need else []

    for start in range(1, len(s) - width + 1):
        outgoing = s[start - 1]
        incoming = s[start + width - 1]

        window[outgoing] -= 1
        if window[outgoing] == 0:
            del window[outgoing]
        window[incoming] += 1

        if window == need:
            result.append(start)

    return result


# --- Re-solve 3 (Day 12): Search in Rotated Sorted Array -----------------
def search_rotated(nums: list[int], target: int) -> int:
    """Return the index of `target` in a rotated strictly-increasing array, or -1."""
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:  # the left half is the sorted one
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # the right half is the sorted one
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


def _max_area_brute(heights: list[int]) -> int:
    """O(n^2) reference for the container problem."""
    best = 0
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            best = max(best, min(heights[i], heights[j]) * (j - i))
    return best


def _find_anagrams_brute(s: str, p: str) -> list[int]:
    """O(n * m log m) reference: sort the window and the pattern, compare."""
    width = len(p)
    target = sorted(p)
    return [
        start
        for start in range(len(s) - width + 1)
        if sorted(s[start : start + width]) == target
    ]


def pop_front_cost(sizes: tuple[int, int] = (2_000, 4_000, 8_000)) -> None:
    """Print the measured cost of `list.pop(0)` next to `deque.popleft()`.

    `list.pop(0)` is O(n): every element after index 0 is shifted one slot
    left. Doubling n therefore quadruples the total time of an n-step queue
    built on it — the quadratic signature. `deque.popleft()` is O(1) because
    the deque stores a block table and only advances a head index.
    """
    print("  n      list.pop(0) total     deque.popleft() total")
    for size in sizes:
        items = list(range(size))
        start = time.perf_counter()
        while items:
            items.pop(0)
        list_elapsed = time.perf_counter() - start

        items = deque(range(size))
        start = time.perf_counter()
        while items:
            items.popleft()
        deque_elapsed = time.perf_counter() - start

        print(f"  {size:<6} {list_elapsed * 1e3:>10.3f} ms {deque_elapsed * 1e3:>17.3f} ms")


def main() -> None:
    """Run the checkpoint checks; all three re-solves must pass."""
    # --- Re-solve 1: statement example and edge cases -------------------
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([]) == 0
    assert max_area([5]) == 0
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2

    rng = random.Random(20261119)
    for _ in range(300):
        size = rng.randint(0, 40)
        heights = [rng.randint(0, 100) for _ in range(size)]
        assert max_area(heights) == _max_area_brute(heights), heights

    # --- Re-solve 2: statement example and edge cases -------------------
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]
    assert find_anagrams("abab", "ab") == [0, 1, 2]
    assert find_anagrams("", "a") == []
    assert find_anagrams("a", "ab") == []
    assert find_anagrams("aa", "aa") == [0]
    assert find_anagrams("abc", "d") == []

    for _ in range(300):
        length = rng.randint(0, 30)
        text = "".join(rng.choice("abc") for _ in range(length))
        pattern = "".join(rng.choice("abc") for _ in range(rng.randint(1, 4)))
        assert find_anagrams(text, pattern) == _find_anagrams_brute(text, pattern), (
            text,
            pattern,
        )

    # --- Re-solve 3: statement example and edge cases -------------------
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1
    assert search_rotated([1], 1) == 0
    assert search_rotated([], 5) == -1
    assert search_rotated([1, 3], 3) == 1
    assert search_rotated([3, 1], 1) == 1

    # Every rotation of every small sorted array, every possible target.
    for size in range(0, 8):
        base = sorted(rng.sample(range(-20, 21), size))
        for rotation in range(size):
            rotated = base[rotation:] + base[:rotation]
            for target in range(-22, 23):
                index = rotated.index(target) if target in rotated else -1
                assert search_rotated(rotated, target) == index, (
                    rotated,
                    target,
                )

    # --- Deliverable 4: the list.pop(0) cost drill ----------------------
    pop_front_cost()

    print("All tests passed.")


if __name__ == "__main__":
    main()
