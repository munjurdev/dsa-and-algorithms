# Contributing

Thanks for helping improve this repository. It is a personal 180-day learning
log first, and a public portfolio second — contributions that keep it honest,
organized, and useful to other learners are welcome.

## Repository conventions

### Folder layout

- One directory per topic, numbered `NN-topic-name/` so files sort in study
  order (e.g. `02-arrays/`, `19-graphs/`).
- Every topic directory contains a `README.md` explaining purpose, core
  concepts, common patterns, and starter problems. Put solutions in the same
  directory, one file per problem.
- Shared material lives in `notes/` (cheatsheets) and `templates/` (reusable
  skeletons). Do not duplicate roadmap content — `ROADMAP.md` is the single
  source of truth for the daily schedule; `PROGRESS.md` is the single source
  of truth for status.

### File and problem naming

```
NNNN-<platform-slug>.py
```

- `NNNN` is a zero-padded sequence number local to the topic folder
  (`0001-two-sum.py`, `0002-valid-parentheses.py`).
- `<platform-slug>` is the problem's slug on its platform
  (`0033-search-in-rotated-sorted-array.py`).
- Mixed/review sets use `NNNN-mixed-<short-description>.py`.
- Never commit a file that is only a copied problem statement with no
  solution of your own.

### Python style

- Python 3.10+, standard library only unless a dependency is justified in
  `requirements.txt`.
- Descriptive names: `left`, `window_count`, `node` — not `i2` or `tmp`.
- Type hints on function signatures: `def two_sum(nums: list[int], target: int) -> list[int]:`.
- 4-space indentation, PEP 8 line length (aim for 88–100), one blank line
  between top-level definitions.
- Prefer `if __name__ == "__main__":` runnable examples over print statements
  scattered through the module.
- No dead code, no commented-out experiments, no debug prints left behind.

### Solution file structure

Every solution starts with the docstring from
[`templates/problem-template.py`](templates/problem-template.py): problem
metadata, approach, *why it works*, complexity, edge cases, tests, and what
you learned. A solution without a complexity analysis will be rejected.

### Testing expectations

- Each solution includes at least 2–3 runnable assertions covering the main
  case and at least one edge case (empty input, single element, duplicates,
  already-sorted data, extremes).
- Tests run with plain `python file.py` (asserts in `__main__`) — no test
  framework required. If you add `pytest`-style tests, put them in
  `tests/` and keep them passing.
- Before opening a PR: `python -m compileall .` and run the tests for every
  file you touched.

## Adding a new problem solution

1. Pick the topic folder that matches the problem's primary pattern.
2. Copy `templates/problem-template.py` to
   `NNNN-<platform-slug>.py` in that folder.
3. Fill in the metadata block, then write the solution with type hints.
4. State the time/space complexity and justify it in the docstring.
5. Add edge-case and test cases under `if __name__ == "__main__":`.
6. Update `PROGRESS.md` counters (only for work you actually finished).
7. Open a pull request describing the problem, your approach, and the
   complexity of your solution.

## Documentation contributions

- Fix typos, broken links, or unclear explanations freely.
- Keep markdown links relative and valid; run a link check before submitting.
- Do not add badges, statistics, or completion claims that are not backed by
  the repository's real state.

## Commit messages

Use the imperative mood and name the scope:

```
feat(09-sliding-window): add min-window-substring solution
docs(16-trees): clarify BFS level-order explanation
fix(10-binary-search): handle empty array in lower_bound helper
```
