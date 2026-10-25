# 09 — Sliding Window

> Phase 4 · Roadmap Days 061–069 · Folder: `09-sliding-window/`

Maintain a contiguous segment that always satisfies a constraint, expanding
right and shrinking left — every element is processed once, so the whole
scan is `O(n)`.

## Purpose

"Longest/shortest subarray or substring with property X" is a sliding-window
problem in disguise. The window replaces the quadratic "check every
substring" enumeration with an invariant you maintain as you move.

## Core concepts

| Concept | Idea in one line | Must be able to... |
|---|---|---|
| Window state | counts, sums, min/max kept incrementally | update state in `O(1)` per move |
| Validity invariant | window always satisfies the constraint | write it in one sentence |
| Fixed window size | exactly `k` elements | running max/min over size-k |
| Variable window | grow until invalid, then shrink | longest-without-repeating-chars |
| At-most → exact | count windows ending at each `right` | convert "at most" into "exactly" |

## Key patterns

1. **Expand/shrink with a counter** — `need` vs `have` for minimum window.
2. **Deque for extremes** — sliding window maximum in `O(n)` (see
   `13-queue-and-deque`).
3. **Shrink to restore balance** — as soon as a constraint breaks, advance
   `left` until it holds again.

## Complexity expectations

- `O(n)` time: each pointer moves at most `n` times.
- `O(k)` space for window state, where `k` = alphabet size or distinct keys.

## Starter problems

| # | Problem | Difficulty | Focus |
|---|---|---|---|
| 1 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | variable window + set/map |
| 2 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | need/have shrinking |
| 3 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | monotonic deque |

## Prerequisites and follow-ups

- **Before this:** `07-two-pointers`, `08-prefix-sum`.
- **Next:** `10-binary-search`.

## Solutions in this folder

| File | Problem | Difficulty | Status |
|---|---|---|---|
| _none yet_ | | | Not started |

Use `templates/problem-template.py` for every new file; see `CONTRIBUTING.md`
for naming rules.
