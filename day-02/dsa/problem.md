# Valid Anagram

| Field | Value |
|---|---|
| Day | `day-02` |
| Track | `dsa` |
| Topic | `00-python-fundamentals` — see `resources/topics/` |
| Difficulty | Easy |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/valid-anagram/ |

## Problem summary

Decide whether two strings are anagrams of each other: `t` must contain
exactly the characters of `s`, each with the same multiplicity, in any order.
The answer is a plain boolean — no rewriting or normalisation of the strings
is required, only a comparison of their character content.

### Input

- `s: str` — the reference string; case-sensitive, may be empty.
- `t: str` — the candidate string; same constraints as `s`.
- Platform bounds: up to 5 × 10⁴ characters each, lowercase English letters
  (the dict approach works for any Unicode characters as well).

### Output

- `bool` — `True` when the two strings are anagrams, `False` otherwise.

## Approach

1. Length guard: different lengths can never be anagrams, so return `False`
   immediately.
2. Walk `s` once, incrementing a `dict[str, int]` frequency map.
3. Walk `t` once, decrementing the same map; if any count drops below zero,
   `t` has a character `s` lacks — return `False` early.
4. If both passes finish with no negative count, every entry is exactly zero
   (equal lengths + all counts ≥ 0 ⇒ all counts = 0), so return `True`.

## Why this approach works

Two strings are anagrams exactly when their character-count maps are equal.
Building the map from `s` and subtracting `t` from it computes the difference
of those two maps in one pass each; a negative entry proves a surplus
character, and equal lengths rule out any deficit, so surviving both passes
means the difference is empty — the maps were identical.

## Complexity

- **Time:** O(n) — one increment pass over `s` and one decrement pass over
  `t`, with O(1) average dict operations.
- **Space:** O(1) — at most 26 entries for lowercase English letters (O(k)
  for k distinct characters in the general case).

## Edge cases

- Both strings empty → `True` (identical multiplicity maps).
- Length mismatch (`"a"` vs `"ab"`) → `False` from the guard, no counting.
- Single character, same/different → `True` / `False`.
- Duplicates matter: `"aabb"` vs `"abbb"` → `False` even though the letter
  sets match — this is why a `set` comparison is wrong.
- Case sensitivity: `"Anagram"` vs `"nagaram"` → `False` (platform is
  case-sensitive; no lowercasing here).

## Test cases

| input | expected | why |
|-------|----------|-----|
| `("anagram", "nagaram")` | `True` | typical anagram |
| `("rat", "car")` | `False` | typical non-anagram |
| `("", "")` | `True` | both empty |
| `("a", "ab")` | `False` | length guard |
| `("a", "b")` | `False` | single-element mismatch |

## What I learned

- **Pattern:** frequency map as the canonical form of a multiset — count
  once, compare the counts.
- **Pitfall:** sorting both strings also works but costs O(n log n); a `set`
  comparison is O(n) yet wrong, because it ignores duplicate counts.
- **Differently next time:** keep the length guard first — it rejects most
  negatives before any allocation happens.

**Review date:** 2026-11-02 (1 day) · 2026-11-08 (7 days) · 2026-12-01 (30 days)
