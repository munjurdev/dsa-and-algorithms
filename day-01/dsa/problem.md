# Reverse Words in a String

| Field | Value |
|---|---|
| Day | `day-01` |
| Track | `dsa` |
| Topic | `00-python-fundamentals` — see `resources/topics/` |
| Difficulty | Easy |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/reverse-words-in-a-string/ |

## Problem summary

Take a sentence in which words are separated by arbitrary runs of whitespace
(leading, trailing, or repeated spaces in the middle) and return it with the
words in reverse order. The output must use exactly one space between words
and no leading or trailing space — the raw whitespace is normalised away, not
preserved.

### Input

- `sentence: str` — letters, digits, and spaces; up to 10⁴ characters.
- A word is a maximal run of non-space characters; runs of one or more
  spaces separate the words.
- The string may start or end with whitespace and may be empty.

### Output

- `str` — the same words reversed, joined by single spaces; `""` when the
  input contains no words.

## Approach

1. Call `str.split()` with no argument: it splits on any whitespace run and
   discards empty pieces, giving the words in original order as a
   `list[str]`.
2. Reverse that list with the slice `words[::-1]`.
3. Join with a single space: `" ".join(reversed_words)`.

## Why this approach works

`split()` with no argument returns exactly the maximal non-whitespace runs of
the input — every word once and nothing else. Reversing that list and joining
with a single space therefore emits each word exactly once, in reverse order,
separated by exactly one space, which is precisely the required output. No
separate whitespace-normalisation step is needed.

## Complexity

- **Time:** O(n) — `split` and `join` each scan all n characters once; the
  reverse is O(k) over the k ≤ n words.
- **Space:** O(n) — the word list holds at most the n characters of the input.

## Edge cases

- `""` or all-whitespace input → `""` (no words to reverse).
- Single word → returned unchanged regardless of surrounding spaces.
- Leading/trailing/repeated spaces → collapsed by `split()`; never reach the
  output.
- Already single-spaced sentence → pure word-order reversal.
- Maximum input (10⁴ characters) → still linear, no recursion involved.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `"the sky is blue"` | `"blue is sky the"` | typical reversal |
| `"  hello   world  "` | `"world hello"` | space runs collapsed |
| `""` | `""` | empty input |
| `"   "` | `""` | whitespace only, zero words |
| `"a"` | `"a"` | single element |

## What I learned

- **Pattern:** normalise first, transform second — `split()` does all the
  whitespace cleanup, so the reversal stays one line.
- **Pitfall:** splitting on a literal `" "` yields empty strings for every
  space run and forces extra filtering.
- **Differently next time:** reach for the built-in (`split`/`join`) before
  writing any character loop.

**Review date:** 2026-11-02 (1 day) · 2026-11-08 (7 days) · 2026-12-01 (30 days)
