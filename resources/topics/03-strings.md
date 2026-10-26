# 03 — Strings

> Phase 2 · Roadmap: see `ROADMAP.md` · File: `resources/topics/03-strings.md`

Strings are arrays of characters with extra rules — immutability, encoding,
and pattern semantics. Most string problems are array problems plus a
normalization step.

## Purpose

Interviews love strings because they hide the data structure: anagram checks
are hashing, palindromes are two pointers, substring search is a window.
This topic makes those translations explicit.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Immutability | Every edit builds a new string | use `"".join(parts)`, never `+=` in loops |
| Normalization | Lowercase, sort, or strip before comparing | detect anagrams in `O(n log n)` |
| Character maps | Frequency dicts over `Counter` | verify anagram in `O(n)` |
| Two-pointer scan | Palindrome / matching from both ends | handle odd/even lengths |
| Runs & encoding | Group consecutive characters | RLE, run-length logic |

## Key patterns

1. **Signature normalization** — `"".join(sorted(s))` as an anagram key.
2. **Index sliding** — convert characters to numeric values for windows.
3. **Build with a list, join once** — avoids quadratic string concatenation.

## Complexity expectations

- String concatenation in a loop is `O(n^2)` — join once for `O(n)`.
- Sliding comparisons should be `O(1)` per move after `O(n)` preprocessing.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | frequency maps |
| 2 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | expand around center |
| 3 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | signature normalization |

## Prerequisites and follow-ups

- **Before this:** `02-arrays`.
- **Next:** `04-matrices`, then hashing and sliding window.

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
