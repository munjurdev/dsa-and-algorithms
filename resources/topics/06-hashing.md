# 06 — Hashing

> Phase 3 · Roadmap: see `ROADMAP.md` · File: `resources/topics/06-hashing.md`

The single highest-leverage technique in interviews: turn an `O(n)` scan per
query into an `O(1)` average lookup by spending memory.

## Purpose

Hash maps and hash sets underpin two-sum, anagram grouping, frequency
counting, caching, and adjacency lists for graphs. If a problem asks "has this
value appeared before?", the answer is almost always a hash table.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Hash map | key → value, `O(1)` average | use `dict` / `defaultdict` / `Counter` |
| Hash set | membership only, `O(1)` average | dedupe and detect collisions fast |
| Frequency map | count occurrences in one pass | two-sum, majority element, anagrams |
| Mapping index by value | `value -> first index` | answer queries about past positions |
| Collisions & worst case | `O(n)` if every key hashes alike | state average vs worst case honestly |

## Key patterns

1. **Seen-set scan** — for each element, check then insert (`O(n)`).
2. **Value → index map** — complement lookups (two-sum family).
3. **Group by signature** — `"".join(sorted(s))` or a frequency tuple keys an
   anagram group.
4. **Prefix + map** — store cumulative sums as you scan (bridge to
   `08-prefix-sum`).

## Complexity expectations

- `O(n)` time, `O(n)` space for essentially every hashing solution — the
  trade *is* the point.
- Building a set inside a nested loop destroys the gain: build it once.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | value → index map |
| 2 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | signature keys |
| 3 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | set lookups, `O(n)` |

## Prerequisites and follow-ups

- **Before this:** Phase 2 (arrays, strings, sorting).
- **Next:** `07-two-pointers`, `08-prefix-sum`.

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
