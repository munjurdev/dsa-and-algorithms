# DSA and Algorithms

A personal, structured **180-day** repository for learning Data Structures and
Algorithms from fundamentals to advanced interview topics, using **Python** as
the primary language.

> **Current status: Day 001 not started.** No problems, days, or phases are
> marked complete anywhere in this repository. Everything you see is the
> scaffolding — the progress is yours to earn and record in
> [`PROGRESS.md`](PROGRESS.md).

## Learning objectives

- Work through a day-by-day roadmap from Python fundamentals to graphs,
  dynamic programming, and advanced topics (Days 001–180).
- Solve problems consistently and document **every** solution: approach, why
  it works, edge cases, time complexity, space complexity.
- Track daily and weekly progress honestly in [`PROGRESS.md`](PROGRESS.md).
- Build a clean, public GitHub portfolio of original work.
- Prepare for technical interviews and competitive problem-solving.

## Technology

| Item | Choice |
|---|---|
| Language | Python 3.10+ (standard library only for solutions) |
| Tooling | Optional: `pytest`, `ruff`, `mypy` (see [`requirements.txt`](requirements.txt)) |
| Practice platforms | LeetCode (primary), plus HackerRank / Codeforces / GeeksforGeeks as needed |

## Repository structure

```
dsa-and-algorithms/
├── README.md              <- you are here
├── ROADMAP.md             <- Day 001–180, the single source of truth for the schedule
├── PROGRESS.md             <- manual daily/weekly tracker (nothing pre-marked)
├── CONTRIBUTING.md         <- naming, style, testing, how to add a solution
├── LICENSE                 <- MIT
├── .gitignore
├── requirements.txt
│
├── 00-python-fundamentals/         ┐
├── 01-complexity-analysis/         │
├── 02-arrays/                      │
├── ...                              │ one folder per topic, each with a
├── 19-graphs/                      │ README: purpose, concepts, patterns,
├── ...                              │ prerequisites, starter problems
├── 27-patterns-and-revision/       ┘
│
├── notes/
│   ├── python-cheatsheet.md
│   ├── complexity-cheatsheet.md
│   ├── problem-solving-patterns.md
│   ├── common-mistakes.md
│   └── lessons-learned.md
│
└── templates/
    ├── problem-template.py         <- copy this for every new solution
    └── topic-template.md
```

Every topic folder has its own `README.md` explaining its purpose, core
concepts, key patterns, and starter problems — start with
[`00-python-fundamentals/README.md`](00-python-fundamentals/README.md).

## Roadmap overview

Full detail lives in [`ROADMAP.md`](ROADMAP.md) — one row per day, every day
from 001 to 180 exactly once.

| Phase | Days | Focus | Days |
|---|---|---|---|
| 1 | 001–015 | Python Fundamentals and Complexity Analysis | 15 |
| 2 | 016–040 | Arrays, Strings, Matrices, and Sorting | 25 |
| 3 | 041–060 | Hashing, Two Pointers, and Prefix Sums | 20 |
| 4 | 061–078 | Sliding Window and Binary Search | 18 |
| 5 | 079–096 | Linked Lists, Stacks, and Queues | 18 |
| 6 | 097–112 | Recursion and Backtracking | 16 |
| 7 | 113–131 | Trees, BSTs, Heaps, and Priority Queues | 19 |
| 8 | 132–150 | Graphs and Graph Algorithms | 19 |
| 9 | 151–168 | Greedy Algorithms and Dynamic Programming | 18 |
| 10 | 169–180 | Advanced Topics, Mixed Practice, and Interview Revision | 12 |

**Built into the schedule:** weekly timed checkpoints (every 7th day), six
mock interviews plus a final one, and buffer days (015, 046, 090, 121, 145,
177) for catching up on hard material.

## Progress summary

| Metric | Value |
|---|---|
| Roadmap days | 180 |
| Completed days | 0 |
| Phases completed | 0 / 10 |
| Problems solved | 0 (Easy 0 · Medium 0 · Hard 0) |

_Update these counters in [`PROGRESS.md`](PROGRESS.md) after each session._

## How to use this repository

1. Read [`ROADMAP.md`](ROADMAP.md) for today's day number — nothing more.
2. Open the topic folder for that day and read its `README.md`.
3. Read the topic material; attempt the suggested problem **before** looking
   at any editorial.
4. Copy [`templates/problem-template.py`](templates/problem-template.py) into
   the topic folder, named per [`CONTRIBUTING.md`](CONTRIBUTING.md).
5. Fill in the docstring (approach, why it works, complexity, edge cases),
   implement, and run the embedded tests.
6. Update `PROGRESS.md`: counters, daily log row, and — if today was a
   checkpoint — the weekly review.

### Daily learning workflow

```
Plan (5 min)   → read today's row in ROADMAP.md, state the goal
Learn (20-30 min) → topic README + notes/ cheatsheets
Solve (30-45 min) → attempt first, then implement in the template
Document (10 min) → approach, complexity, edge cases, review date
Log (5 min)    → PROGRESS.md counters + daily row
```

### Progress tracking instructions

- Only `PROGRESS.md` holds status. Never pre-mark a day.
- Count a problem as solved only if you can re-derive it from a blank file.
- Weekly: fill the *Weekly review log* row for the week that just ended.
- When a topic still feels shaky, add it to *Topics requiring revision* with
  a next-review date.

### Problem difficulty conventions

- **Easy** — the direct idea; usually one pass or one structure.
- **Medium** — combines two ideas, or needs a non-obvious invariant.
- **Hard** — multiple insights, heavy implementation, or deep DP/graphs.
- The difficulty shown in the roadmap is the platform's rating for the
  suggested problem.

## Running Python solutions

```bash
# from the repository root
python 02-arrays/0001-two-sum.py
```

Every solution is self-testing: it ends with `assert`s and prints
`All tests passed.` No framework is required. Optional tooling:

```bash
pip install -r requirements.txt   # pytest / ruff / mypy, if you choose to use them
python -m compileall .            # syntax check everything
```

## Contributing

Fixes to docs, broken links, and clarified explanations are welcome — see
[`CONTRIBUTING.md`](CONTRIBUTING.md) for naming, Python style, testing
expectations, and the checklist for adding a solution. If you fork this to
run your own 180-day cycle, keep `PROGRESS.md` honest and start the counters
from zero.

## Learning resources

- [LeetCode](https://leetcode.com) — primary problem source (patterns,
  companies, and daily challenges)
- [NeetCode](https://neetcode.io) — curated pattern-ordered problem lists
- [Python official tutorial](https://docs.python.org/3/tutorial/) — language
  reference
- [Big-O cheat sheet](https://www.bigocheatsheet.com/) — complexity reference
- In-repo: `notes/python-cheatsheet.md`, `notes/complexity-cheatsheet.md`,
  `notes/problem-solving-patterns.md`, `notes/common-mistakes.md`

## License

Released under the [MIT License](LICENSE) — see it for the full text.
Replace the `<YOUR NAME OR GITHUB USERNAME>` placeholder before publishing.
