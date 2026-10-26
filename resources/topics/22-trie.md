# 22 — Trie (Prefix Tree)

> Phase 10 · Roadmap: see `ROADMAP.md` · File: `resources/topics/22-trie.md`

A tree of characters where each path from the root is a shared prefix —
built once, queried for every prefix in `O(length)`.

## Purpose

Tries turn "does any word start with this prefix?" and "how many words match
this pattern?" into simple tree walks, and they are the classic answer to
autocomplete, word-search-board, and dictionary problems where a hash set
would need every suffix.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Node with children | fixed 26-slot array or dict of children | trade memory for speed |
| End-of-word flag | nodes mark terminals explicitly | distinguish "prefix" from "word" |
| Prefix count field | store counts at nodes | answer "k words with this prefix" |
| Walk from root | one node per character consumed | handle missing branches gracefully |
| Trie as DP target | walk/DFS over trie + text together | word-break and string-matching variants |

## Key patterns

1. **Insert then search** — build the dictionary once, query many.
2. **DFS over trie × grid** — find all dictionary words in a board
   (backtracking + trie pruning).
3. **XOR trie (advanced)** — bitwise tries for maximum XOR; noted for
   extension, not core scope.

## Complexity expectations

- Insert/search `O(L)` for a string of length `L` — independent of how many
  words are stored (a hash set costs `O(L)` per query too, but can't answer
  prefix-count questions).

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | insert / search / startsWith |
| 2 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | trie-guided backtracking on a grid |
| 3 | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Medium | sort + prefix walk or trie |

## Prerequisites and follow-ups

- **Before this:** `15-backtracking`, `16-trees`, `03-strings`.
- **Next:** `24-bit-manipulation`, `25-intervals`.

## Solutions

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Solutions for this topic live under `day-NN/dsa/` and `day-NN/algorithms/`,
scaffolded from `templates/` — see `CONTRIBUTING.md` for naming rules.
