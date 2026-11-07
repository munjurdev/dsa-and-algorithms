# Valid Palindrome

| Field | Value |
|---|---|
| Day | `day-05` |
| Track | `dsa` |
| Topic | `03-strings` — see `resources/topics/` |
| Difficulty | Easy |
| Platform | LeetCode |
| URL | https://leetcode.com/problems/valid-palindrome/ |

## Problem summary

Decide whether a string reads the same forwards and backwards after
lowercasing it and dropping every character that is not an **ASCII** letter or
digit. Spaces, punctuation, and underscores are ignored, so
`"A man, a plan, a canal: Panama"` is valid while `"race a car"` is not. Two
variants are implemented and must agree on every input: an in-place
two-pointer scan (`O(1)` extra space) and a normalize-then-compare version
(`O(n)` space).

### Input

- `s: str` — `1 <= len(s) <= 2×10⁵`; any printable ASCII, and possibly
  non-ASCII characters (which the problem does **not** treat as alphanumeric).
- A string with no letters or digits at all (e.g. `" "`) is valid input.

### Output

- `bool` — `True` if the cleaned string equals its reverse, else `False`.

## Approach

**Variant 1 — two pointers, `is_palindrome`:**

1. Put `left` at the first index and `right` at the last index.
2. Advance `left` while it points at a non-alphanumeric character and
   `left < right`; retreat `right` the same way.
3. Compare `s[left].lower()` with `s[right].lower()`. A mismatch means the
   string is not a palindrome — return `False`.
4. Otherwise step both pointers inward and repeat from step 2.
5. When the pointers meet or cross, every mirrored pair matched → `True`.

**Variant 2 — normalize then compare, `is_palindrome_normalized`:**

1. Build `cleaned` by keeping only ASCII alphanumerics, lowercased.
2. Return `cleaned == cleaned[::-1]`.

Both variants share one predicate, `_is_ascii_alphanumeric`
(`char.isascii() and char.isalnum()`), so they differ only in *where* they
skip and reverse — never in what counts as alphanumeric.

## Why this approach works

The skip loops in variant 1 leave `left` and `right` on the `i`-th kept
character from the front and the `i`-th kept character from the back, for
`i = 0, 1, 2, …`. So each comparison is exactly the comparison
`cleaned[i] == cleaned[-1 - i]` that variant 2 performs as a whole-string
check. Therefore the two-pointer version returns `False` at the first position
where the cleaned string and its reverse differ, and `True` only once every
mirrored pair has matched — the definition of a palindrome. Stopping the skip
loops on `left < right` is what makes an all-punctuation string (`" "`,
`".,"`) terminate and correctly return `True` instead of running a pointer
past the other.

## Complexity

- **Time:** O(n) — each character is examined at most once per pointer
  (variant 1), or once by the filter plus once by the reverse comparison
  (variant 2).
- **Space:** O(1) auxiliary for `is_palindrome` (two indices); O(n) for
  `is_palindrome_normalized` (the cleaned copy).

## Edge cases

- No alphanumerics: `" "` and `".,"` → `True`: the cleaned string is empty,
  and the empty string is its own reverse. The `left < right` guard in both
  skip loops is what prevents an out-of-range index here.
- Empty input `""` → `True` (outside LeetCode's constraints, but the function
  is total and must not crash).
- Single character: `"a"` → `True`; `"!"` → `True` (cleans to empty).
- Case folding only applies to letters: `"Aa"` → `True`, `"0P"` → `False`
  (`'0'` vs `'p'`), `"1a2"` → `False`.
- Punctuation inside a palindrome: `"ab_a"` → `"aba"` → `True`; comparing the
  raw string without filtering would wrongly say `False`.
- Unicode: `"Éa"` → `True`, because LeetCode counts only ASCII
  alphanumerics, so only `"a"` survives. Using bare `str.isalnum()` keeps
  `'É'` and flips the answer to `False` — the reason for the `isascii()`
  guard.
- Both parities: `"abba"` and `"aba"` → `True`.
- Maximum length (`2×10⁵`): a single linear pass, no recursion and no slicing
  in the `O(1)` variant, so no quadratic concatenation or stack depth.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `"A man, a plan, a canal: Panama"` | `True` | the statement's example |
| `"race a car"` | `False` | the statement's negative example |
| `" "` | `True` | cleans to the empty string |
| `".,"` | `True` | punctuation only, still empty after cleaning |
| `""` | `True` | empty string is a palindrome |
| `"a"` / `"!"` | `True` / `True` | single char: letter and punctuation |
| `"Aa"` | `True` | case is ignored |
| `"0P"` | `False` | digits are kept, so `'0'` ≠ `'p'` |
| `"ab_a"` | `True` | underscore is dropped: `"aba"` |
| `"Éa"` | `True` | non-ASCII letters are dropped, not folded |
| `"abba"` / `"aba"` | `True` / `True` | even and odd lengths |
| `"1a2"` | `False` | digits break the mirror |
| every string of length ≤ 4 over `a A 0 _ . space` | both variants equal an inline reference | exhaustive three-way agreement |
| 300 random strings (length ≤ 40, letters + digits + punctuation) | both variants equal an inline reference | randomized three-way agreement |
| a `2×10⁵`-character string | runs in one pass | constraint sanity check |

## What I learned

- **Pattern:** a palindrome is a two-pointer problem, but only *after*
  normalization — decide what "kept" means first, then both variants fall out
  of that one predicate.
- **Pitfall:** `str.isalnum()` is Unicode-aware, so `'É'` and `'²'` count as
  alphanumeric; LeetCode wants ASCII only. `isascii() and isalnum()` is the
  honest test.
- **Differently next time:** write the filter predicate before either variant.
  Sharing it is what makes "the two variants agree" a fact I can test rather
  than hope for.

**Review date:** 2026-11-08 (1 day) · 2026-11-14 (7 days) · 2026-12-07 (30 days)
