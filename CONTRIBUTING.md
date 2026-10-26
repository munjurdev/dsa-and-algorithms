# Contributing

Thanks for helping improve this repository. It is a personal 30-day learning
log first, and a public portfolio second — contributions that keep it honest,
organized, and useful to other learners are welcome.

## Repository conventions

### Folder layout

- One directory per study day, numbered `day-NN/` (`day-01/` … `day-30/`), so
  files sort in study order.
- Every day has exactly two track folders, `dsa/` and `algorithms/`, each
  holding two files:
  - `problem.md` — the write-up: metadata, summary, approach, *why it works*,
    complexity, edge cases, tests, and what you learned.
  - `solution.py` — the code, self-testing.
- Topic material (purpose, concepts, patterns, starter problems) lives in
  `resources/topics/NN-topic-name.md`; cheatsheets and reference notes live in
  `resources/`. Shared material lives in `templates/` (reusable skeletons).
- Do not duplicate roadmap content — `ROADMAP.md` is the single source of
  truth for the daily schedule; `PROGRESS.md` is the single source of truth
  for status.

### File and problem naming

```
day-NN/<track>/problem.md
day-NN/<track>/solution.py
```

- `<track>` is `dsa` or `algorithms`; `NN` is the day from `ROADMAP.md`
  (`day-07/dsa/solution.py`).
- One problem per track per day is the default. If a day needs more, number
  the extras so each pair stays together: `problem-2.md` + `solution-2.py`.
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

Every problem has two files, copied from the templates:

- [`templates/problem-template.md`](templates/problem-template.md) →
  `problem.md`: problem metadata, summary, approach, *why it works*,
  complexity, edge cases, the test table, and the review date.
- [`templates/problem-template.py`](templates/problem-template.py) →
  `solution.py`: a short docstring (approach in one paragraph, both
  complexities) plus the implementation.

A solution without a complexity analysis in `problem.md` will be rejected.

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

1. Find today's row in `ROADMAP.md` and open the matching `day-NN/` folder —
   or, for extra practice, the `dsa/` or `algorithms/` folder of the day whose
   topic it belongs to.
2. Copy `templates/problem-template.md` → `problem.md` and
   `templates/problem-template.py` → `solution.py` in that folder (use
   `problem-2.md` / `solution-2.py` if the default pair is taken).
3. Fill in `problem.md` first: metadata, approach, *why it works*.
4. Write the solution with type hints.
5. State the time/space complexity in `problem.md` and justify it.
6. Add edge-case and test cases under `if __name__ == "__main__":`.
7. Update `PROGRESS.md` counters (only for work you actually finished).
8. Open a pull request describing the problem, your approach, and the
   complexity of your solution.

## Documentation contributions

- Fix typos, broken links, or unclear explanations freely.
- Keep markdown links relative and valid; run a link check before submitting.
- Do not add badges, statistics, or completion claims that are not backed by
  the repository's real state.

## Commit messages

Use the imperative mood and name the scope:

```
feat(day-07): add two-sum solution
docs(resources/topics/16-trees): clarify BFS level-order explanation
fix(day-12): handle empty array in lower_bound helper
```
