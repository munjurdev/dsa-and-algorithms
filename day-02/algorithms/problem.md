# Word-frequency analyzer capstone

| Field | Value |
|---|---|
| Day | `day-02` |
| Track | `algorithms` |
| Topic | `00-python-fundamentals` — see `resources/topics/` |
| Difficulty | Medium |
| Platform | Other (self-made capstone) |
| URL | _none — self-made_ |

## Problem summary

A capstone that turns raw text into a ranked word report, built from small
pure typed functions: `tokenize` lowercases the text and extracts its
letter/digit runs, `word_counts` tallies the tokens in one pass, `top_words`
ranks the counts with a deterministic tie-break, `filter_words` keeps long
words via a comprehension, and `summarize` composes the first three into
`(word, count)` pairs. Every function takes its input and returns a new
value — nothing is mutated and nothing is printed inside the functions.

### Input

- `text: str` — any raw string; empty input is allowed.
- `words: list[str]` — tokens, already normalised by `tokenize`.
- `counts: dict[str, int]` — a frequency map, e.g. from `word_counts`.
- `k: int` — how many top words to return (`0` gives an empty list).
- `min_length: int` — minimum word length for the filter.

### Output

- `tokenize` → `list[str]`; `word_counts` → `dict[str, int]`;
  `top_words` → `list[str]`; `filter_words` → `dict[str, int]`;
  `summarize` → `list[tuple[str, int]]`.

## Approach

1. **`tokenize(text)`** — one `re.findall(r"[a-z0-9]+", text.lower())` pass:
   lowercasing folds case, the regex discards punctuation and returns the
   word runs in order.
2. **`word_counts(words)`** — single loop, `counts[word] =
   counts.get(word, 0) + 1`; each token increments exactly once.
3. **`top_words(counts, k)`** — guard clause for `k <= 0`, then sort items by
   `(-count, word)` and slice the first `k`, returning just the words.
4. **`filter_words(counts, min_length)`** — dict comprehension over
   `sorted(counts.items())`, keeping entries with `len(word) >= min_length`.
5. **`summarize(text, k)`** — chain `tokenize` → `word_counts` → `top_words`
   and pair each winner with its count from the map.

## Why this approach works

`word_counts` is exact by construction: the loop visits every token once and
increments its entry once, so the map equals the true multiplicity of each
word. `top_words` prefixes a total order — `(-count, word)` never ties — so
the selected `k` words are uniquely determined. Composing exact, pure
functions keeps the composition exact: `summarize` adds no counting logic of
its own, only lookups into the already-correct map.

## Complexity

- **`tokenize` — Time:** O(n) — one regex scan over n characters.
- **`word_counts` — Time:** O(m) — one pass over m tokens, O(1) dict ops.
- **`top_words` / `filter_words` — Time:** O(u log u) — sorting the u
  distinct words.
- **`summarize` — Time:** O(n + m + u log u) — the chain of the above.
- **Space:** O(m + u) — the token list plus one counter entry per distinct
  word (outputs add at most `k` entries).

## Edge cases

- Empty text → `tokenize` returns `[]`, `word_counts` returns `{}`,
  `summarize` returns `[]`.
- `k = 0` → `[]`; `k` larger than the number of distinct words → all of them
  (slicing never raises).
- Equal frequencies → alphabetical order, so repeated runs agree.
- Case and punctuation folded by `tokenize`: `"Hello, HELLO!"` → two
  `"hello"` tokens.
- Apostrophes and hyphens split words (`"don't"` → `don`, `t`) — a documented
  tokenizer rule, not a bug.
- Stopwords are **not** removed — out of scope for this drill; noted as the
  natural extension.

## Test cases

| input | expected | why |
|-------|----------|-----|
| `tokenize("Hello, HELLO!")` | `["hello", "hello"]` | case + punctuation folded |
| `word_counts(["the", "cat", "the"])` | `{"the": 2, "cat": 1}` | one-pass counts |
| `word_counts([])` | `{}` | empty input |
| `top_words(counts, 2)` | `["the", "cat"]` | typical ranking |
| `top_words(counts, 0)` | `[]` | `k = 0` |
| `top_words({"b": 2, "a": 2}, 2)` | `["a", "b"]` | tie → alphabetical |
| `filter_words(counts, 4)` | `{}` | comprehension filter, all shorter |

## What I learned

- **Pattern:** small pure functions compose — tokenize, count, and rank can
  each be tested alone, so the capstone needs almost no new logic.
- **Pitfall:** dict iteration order is insertion order, not frequency order;
  the explicit sort is what makes `top_words` deterministic.
- **Differently next time:** document the tokenizer rule up front (splits on
  apostrophes) and refactor the counting line to `Counter` once the manual
  dict version is understood.

**Review date:** 2026-11-02 (1 day) · 2026-11-08 (7 days) · 2026-12-01 (30 days)
