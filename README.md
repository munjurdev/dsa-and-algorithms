# DSA and Algorithms

A personal, structured **30-day** repository for learning Data Structures and
Algorithms from fundamentals to advanced interview topics, using **Python** as
the primary language.

> **Current status: Day 08 of 30 complete.** Phases 1 and 2 are finished and
> recorded in [`PROGRESS.md`](PROGRESS.md); weekly checkpoint 01 passed, and
> Day 09 continues Phase 3. The counters below are updated after each session —
> never in advance.

## Learning objectives

- Work through a day-by-day roadmap from Python fundamentals to graphs,
  dynamic programming, and advanced topics (Days 01–30).
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
├── ROADMAP.md             <- Day 01–30, the single source of truth for the schedule
├── PROGRESS.md             <- manual daily/weekly tracker (nothing pre-marked)
├── CONTRIBUTING.md         <- naming, style, testing, how to add a solution
├── LICENSE                 <- MIT
├── .gitignore
├── requirements.txt
│
├── day-01/
│   ├── dsa/
│   │   ├── problem.md      <- write-up: summary, approach, complexity, tests
│   │   └── solution.py     <- the code, self-testing
│   └── algorithms/
│       ├── problem.md
│       └── solution.py
├── day-02/
│   ├── dsa/
│   └── algorithms/
├── ...
├── day-30/
│   ├── dsa/
│   └── algorithms/
│
├── resources/
│   ├── complexity-cheatsheet.md
│   ├── problem-solving-patterns.md
│   ├── python-cheatsheet.md
│   ├── common-mistakes.md
│   ├── lessons-learned.md
│   └── topics/                    <- one write-up per topic, 00–27:
│       ├── 00-python-fundamentals.md
│       ├── 01-complexity-analysis.md
│       ├── 02-arrays.md
│       └── ... 27-patterns-and-revision.md
│
└── templates/
    ├── problem-template.md        <- copy this into day-NN/<track>/problem.md
    ├── problem-template.py        <- copy this into day-NN/<track>/solution.py
    └── topic-template.md
```

Every topic write-up in [`resources/topics/`](resources/topics/) explains its
purpose, core concepts, key patterns, and starter problems — start with
[`resources/topics/00-python-fundamentals.md`](resources/topics/00-python-fundamentals.md).

## Roadmap overview

Full detail lives in [`ROADMAP.md`](ROADMAP.md) — one row per day, every day
from 01 to 30 exactly once, and each row says what belongs in `dsa/` and in
`algorithms/`.

| Phase | Days | Focus | Days |
|---|---|---|---|
| 1 | 01–03 | Python Fundamentals and Complexity Analysis | 3 |
| 2 | 04–06 | Arrays, Strings, Matrices, and Sorting | 3 |
| 3 | 07–09 | Hashing, Two Pointers, and Prefix Sums | 3 |
| 4 | 10–12 | Sliding Window and Binary Search | 3 |
| 5 | 13–15 | Linked Lists, Stacks, and Queues | 3 |
| 6 | 16–18 | Recursion and Backtracking | 3 |
| 7 | 19–21 | Trees, BSTs, Heaps, and Priority Queues | 3 |
| 8 | 22–24 | Graphs and Graph Algorithms | 3 |
| 9 | 25–27 | Greedy Algorithms and Dynamic Programming | 3 |
| 10 | 28–30 | Advanced Topics, Mixed Practice, and Interview Revision | 3 |

**Built into the schedule:** weekly timed checkpoints (Days 007, 014, 021,
028), two mock interviews (Days 015 and 030), and a phase boundary every third
day for consolidation.

## Progress summary

| Metric | Value |
|---|---|
| Roadmap days | 30 |
| Completed days | 8 |
| Phases completed | 2 / 10 |
| Problems solved | 15 (Easy 7 · Medium 8 · Hard 0) |

_Update these counters in [`PROGRESS.md`](PROGRESS.md) after each session._

## How to use this repository

1. Read today's row in [`ROADMAP.md`](ROADMAP.md) — nothing more.
2. Read the topic write-up it names, in [`resources/topics/`](resources/topics/),
   plus the relevant cheatsheet in [`resources/`](resources/).
3. Attempt the suggested problem **before** looking at any editorial.
4. Copy [`templates/problem-template.md`](templates/problem-template.md) and
   [`templates/problem-template.py`](templates/problem-template.py) into the
   day's `dsa/` or `algorithms/` folder, named `problem.md` and `solution.py`
   (see [`CONTRIBUTING.md`](CONTRIBUTING.md) for extras).
5. Fill in `problem.md` (approach, why it works, complexity, edge cases),
   implement in `solution.py`, and run the embedded tests.
6. Update `PROGRESS.md`: counters, daily log row, and — at Days 007, 014,
   021, 028 — the weekly review.

### Daily learning workflow

```
Plan (5 min)   → read today's row in ROADMAP.md, state the goal
Learn (20-30 min) → topic write-up + resources/ cheatsheets
Solve (30-45 min) → attempt first, then implement from the templates
Document (10 min) → problem.md: approach, complexity, edge cases, review date
Log (5 min)    → PROGRESS.md counters + daily row
```

### Progress tracking instructions

- Only `PROGRESS.md` holds status. Never pre-mark a day.
- Count a problem as solved only if you can re-derive it from a blank file.
- At each checkpoint (Days 007, 014, 021, 028), fill the *Weekly review log*
  row for the week that just ended.
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
python day-01/dsa/solution.py
python day-30/algorithms/solution.py
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
run your own 30-day cycle, keep `PROGRESS.md` honest and start the counters
from zero.

## Learning resources

- [LeetCode](https://leetcode.com) — primary problem source (patterns,
  companies, and daily challenges)
- [NeetCode](https://neetcode.io) — curated pattern-ordered problem lists
- [Python official tutorial](https://docs.python.org/3/tutorial/) — language
  reference
- [Big-O cheat sheet](https://www.bigocheatsheet.com/) — complexity reference
- In-repo: `resources/python-cheatsheet.md`, `resources/complexity-cheatsheet.md`,
  `resources/problem-solving-patterns.md`, `resources/common-mistakes.md`

## License

Released under the [MIT License](LICENSE) — see it for the full text.
Replace the `<YOUR NAME OR GITHUB USERNAME>` placeholder before publishing.
