"""
Solution for: Classify 10 snippets + justify list.append amortization
Day:      day-03
Track:    algorithms
Difficulty: Easy

Full write-up (summary, approach, edge cases, tests, review date) lives in
`problem.md` next to this file. Keep only the essentials here.

Approach (one paragraph):
    Each snippet is scored by an `ast`-based classifier that tracks a cost
    pair (a, b) meaning n^a · (log n)^b: a loop multiplies the body by
    (1, 0), a `while` that halves its induction variable by (0, 1),
    sequential statements keep the dominant pair, `sorted`/`.sort()` cost
    (1, 1) and a list membership test costs (1, 0) while hash-collection
    membership costs (0, 0). `main()` scores all ten snippets against the
    expected table (10/10 required, each with a one-line justification) and
    proves the append amortization: capacity doubling copies at most 2n
    elements over n appends.

Time Complexity:  O(S)   # S = snippet source size, one AST pass per snippet
Space Complexity: O(D)   # D = AST depth of the deepest snippet (recursion)

Review Date:  2026-11-03 / 2026-11-09 / 2026-12-02
"""

from __future__ import annotations

import ast
import textwrap
from collections.abc import Iterable
from dataclasses import dataclass

Exp = tuple[int, int]  # cost n^a · (log n)^b

_CONSTANT: Exp = (0, 0)
_LOOP: Exp = (1, 0)
_LOG: Exp = (0, 1)
_SORT: Exp = (1, 1)

_CONSTANT_CALLS = frozenset(
    {
        "abs", "bool", "chr", "enumerate", "float", "hash", "int", "len",
        "ord", "print", "range", "repr", "round", "str", "zip",
    }
)
_LINEAR_CALLS = frozenset({"all", "any", "list", "max", "min", "set", "sum", "tuple"})
_CONSTANT_METHODS = frozenset(
    {"add", "append", "get", "items", "keys", "pop", "values"}
)
_LINEAR_METHODS = frozenset({"extend", "join"})
_HASH_BUILDERS = frozenset({"dict", "frozenset", "set"})


def _dominant(left: Exp, right: Exp) -> Exp:
    """Sum of two cost terms is bounded by the faster-growing one."""
    return max(left, right)


def _product(left: Exp, right: Exp) -> Exp:
    """Product of two cost terms adds their exponents."""
    return (left[0] + right[0], left[1] + right[1])


def _statements_cost(statements: Iterable[ast.stmt]) -> Exp:
    """Sequential statements cost their dominant member."""
    cost = _CONSTANT
    for statement in statements:
        cost = _dominant(cost, _statement_cost(statement))
    return cost


def _statement_cost(node: ast.stmt) -> Exp:
    """Worst-case cost of one statement, loops multiplying their body."""
    if isinstance(node, (ast.For, ast.AsyncFor)):
        body = _dominant(_statements_cost(node.body), _statements_cost(node.orelse))
        return _dominant(_product(body, _LOOP), _expression_cost(node.iter))
    if isinstance(node, ast.While):
        body = _dominant(_statements_cost(node.body), _statements_cost(node.orelse))
        factor = _LOG if _halves_induction(node) else _LOOP
        return _dominant(_product(body, factor), _expression_cost(node.test))
    if isinstance(node, ast.If):
        cost = _dominant(_statements_cost(node.body), _statements_cost(node.orelse))
        return _dominant(cost, _expression_cost(node.test))
    if isinstance(node, (ast.With, ast.AsyncWith)):
        cost = _CONSTANT
        for item in node.items:
            cost = _dominant(cost, _expression_cost(item.context_expr))
        return _dominant(cost, _statements_cost(node.body))
    if isinstance(node, (ast.Return, ast.Assign, ast.AugAssign, ast.Expr)):
        value = getattr(node, "value", None)
        return _expression_cost(value)
    if isinstance(node, ast.AnnAssign):
        return _expression_cost(node.value)
    if isinstance(node, ast.Assert):
        return _expression_cost(node.test)
    if isinstance(node, ast.Raise):
        return _expression_cost(node.exc)
    if isinstance(
        node,
        (
            ast.Pass, ast.Break, ast.Continue, ast.Delete, ast.Global,
            ast.Nonlocal, ast.Import, ast.ImportFrom,
        ),
    ):
        return _CONSTANT
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return _CONSTANT  # a nested def only binds a function object
    raise ValueError(f"unsupported statement: {type(node).__name__}")


def _halves_induction(node: ast.While) -> bool:
    """True when the body divides a variable by a constant (binary search)."""
    for statement in node.body:
        for child in ast.walk(statement):
            if isinstance(child, (ast.Assign, ast.AugAssign)) and _divides_by_constant(
                child.value
            ):
                return True
    return False


def _divides_by_constant(node: ast.expr | None) -> bool:
    """True for `x = x // 2`, `x /= 2`, `x >>= 1` and friends."""
    if not isinstance(node, ast.BinOp):
        return False
    if not isinstance(node.op, (ast.FloorDiv, ast.Div, ast.RShift)):
        return False
    right = node.right
    if not isinstance(right, ast.Constant) or not isinstance(right.value, int):
        return False
    minimum = 1 if isinstance(node.op, ast.RShift) else 2
    return right.value >= minimum


def _membership_cost(collection: ast.expr) -> Exp:
    """Scanning a list costs n; hashing into a set/dict costs one lookup."""
    if isinstance(collection, (ast.Set, ast.Dict)):
        return _CONSTANT
    if (
        isinstance(collection, ast.Call)
        and isinstance(collection.func, ast.Name)
        and collection.func.id in _HASH_BUILDERS
    ):
        return _CONSTANT
    return _LOOP


def _comprehension_cost(
    node: ast.ListComp | ast.SetComp | ast.DictComp | ast.GeneratorExp,
) -> Exp:
    """A comprehension costs its body per element of every generator."""
    if isinstance(node, ast.DictComp):
        cost = _dominant(_expression_cost(node.key), _expression_cost(node.value))
    else:
        cost = _expression_cost(node.elt)
    for generator in node.generators:
        for condition in generator.ifs:
            cost = _dominant(cost, _expression_cost(condition))
        cost = _dominant(_product(cost, _LOOP), _expression_cost(generator.iter))
    return cost


def _call_cost(node: ast.Call) -> Exp:
    """Known calls have fixed costs; unknown ones fail loudly."""
    arguments = _CONSTANT
    for argument in node.args:
        arguments = _dominant(arguments, _expression_cost(argument))
    for keyword in node.keywords:
        arguments = _dominant(arguments, _expression_cost(keyword.value))

    function = node.func
    if isinstance(function, ast.Name):
        if function.id == "sorted":
            return _dominant(arguments, _SORT)
        if function.id in _LINEAR_CALLS:
            return _dominant(arguments, _LOOP)
        if function.id in _CONSTANT_CALLS:
            return arguments
        raise ValueError(f"unsupported function call: {function.id!r}")
    if isinstance(function, ast.Attribute):
        receiver = _expression_cost(function.value)
        if function.attr == "sort":
            return _dominant(_dominant(arguments, _SORT), receiver)
        if function.attr in _LINEAR_METHODS:
            return _dominant(_dominant(arguments, _LOOP), receiver)
        if function.attr in _CONSTANT_METHODS:
            return _dominant(arguments, receiver)
        raise ValueError(f"unsupported method call: {function.attr!r}")
    raise ValueError("unsupported call target")


def _expression_cost(node: ast.expr | None) -> Exp:
    """Worst-case cost of evaluating one expression."""
    if node is None or isinstance(node, (ast.Constant, ast.Name, ast.Lambda)):
        return _CONSTANT
    if isinstance(node, ast.UnaryOp):
        return _expression_cost(node.operand)
    if isinstance(node, ast.BinOp):
        return _dominant(_expression_cost(node.left), _expression_cost(node.right))
    if isinstance(node, ast.BoolOp):
        cost = _CONSTANT
        for value in node.values:
            cost = _dominant(cost, _expression_cost(value))
        return cost
    if isinstance(node, ast.Compare):
        cost = _expression_cost(node.left)
        for operator, comparator in zip(node.ops, node.comparators):
            if isinstance(operator, (ast.In, ast.NotIn)):
                cost = _dominant(cost, _membership_cost(comparator))
            cost = _dominant(cost, _expression_cost(comparator))
        return cost
    if isinstance(node, ast.IfExp):
        return max(
            _expression_cost(node.test),
            _expression_cost(node.body),
            _expression_cost(node.orelse),
        )
    if isinstance(node, ast.Subscript):
        return _dominant(_expression_cost(node.value), _expression_cost(node.slice))
    if isinstance(node, ast.Attribute):
        return _expression_cost(node.value)
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        cost = _CONSTANT
        for element in node.elts:
            cost = _dominant(cost, _expression_cost(element))
        return cost
    if isinstance(node, ast.Dict):
        cost = _CONSTANT
        for key, value in zip(node.keys, node.values):
            cost = _dominant(cost, _expression_cost(key))
            cost = _dominant(cost, _expression_cost(value))
        return cost
    if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
        return _comprehension_cost(node)
    if isinstance(node, ast.Call):
        return _call_cost(node)
    if isinstance(node, ast.Starred):
        return _expression_cost(node.value)
    if isinstance(node, ast.NamedExpr):
        return _expression_cost(node.value)
    raise ValueError(f"unsupported expression: {type(node).__name__}")


def _format(cost: Exp) -> str:
    """Render (a, b) as the Big-O label for n^a · (log n)^b."""
    power, log_power = cost
    if power == 0 and log_power == 0:
        return "O(1)"
    if power == 0 and log_power == 1:
        return "O(log n)"
    if power == 0:
        return f"O(log^{log_power} n)"
    size = "n" if power == 1 else f"n^{power}"
    if log_power == 0:
        return f"O({size})"
    if log_power == 1:
        return f"O({size} log n)"
    return f"O({size} log^{log_power} n)"


def classify(code: str) -> str:
    """Return the worst-case Big-O label of the function defined in `code`.

    Args:
        code: a snippet containing exactly one function definition.

    Returns:
        A label such as `"O(n^2)"`.

    Raises:
        ValueError: if there is no function, or a construct the rules do
            cover is used (unknown calls, unsupported statements).
    """
    tree = ast.parse(textwrap.dedent(code))
    functions = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    if not functions:
        raise ValueError("no function definition found")
    cost = _CONSTANT
    for function in functions:
        cost = _dominant(cost, _statements_cost(function.body))
    return _format(cost)


@dataclass(frozen=True)
class Snippet:
    """One graded drill entry: source, expected label, one-line justification."""

    name: str
    code: str
    expected: str
    justification: str


SNIPPETS: tuple[Snippet, ...] = (
    Snippet(
        name="constant_length",
        code="""
            def f(xs):
                return len(xs)
        """,
        expected="O(1)",
        justification="len() reads a field stored on the list, so it never scans.",
    ),
    Snippet(
        name="constant_index",
        code="""
            def f(xs):
                return xs[0] + xs[-1]
        """,
        expected="O(1)",
        justification="Indexing is address arithmetic: one step regardless of size.",
    ),
    Snippet(
        name="binary_search",
        code="""
            def f(xs, target):
                low, high = 0, len(xs) - 1
                while low <= high:
                    middle = (low + high) // 2
                    if xs[middle] == target:
                        return middle
                    if xs[middle] < target:
                        low = middle + 1
                    else:
                        high = middle - 1
                return -1
        """,
        expected="O(log n)",
        justification="Each comparison halves the remaining range, so ~log2(n) steps.",
    ),
    Snippet(
        name="linear_sum",
        code="""
            def f(xs):
                total = 0
                for value in xs:
                    total += value
                return total
        """,
        expected="O(n)",
        justification="One pass with constant work per element.",
    ),
    Snippet(
        name="linear_search",
        code="""
            def f(xs, target):
                for index, value in enumerate(xs):
                    if value == target:
                        return index
                return -1
        """,
        expected="O(n)",
        justification="Worst case scans every element once; Big-O is the worst case.",
    ),
    Snippet(
        name="two_passes",
        code="""
            def f(xs):
                first_total = 0
                for value in xs:
                    first_total += value
                second_total = 0
                for value in xs:
                    second_total += first_total
                return second_total
        """,
        expected="O(n)",
        justification="Two linear passes are still linear; constant factors drop out.",
    ),
    Snippet(
        name="pair_count",
        code="""
            def f(xs):
                pairs = 0
                for first in xs:
                    for second in xs:
                        pairs += 1
                return pairs
        """,
        expected="O(n^2)",
        justification="The inner loop runs once per outer element: n*n pairs.",
    ),
    Snippet(
        name="filtered_copy",
        code="""
            def f(xs, seen):
                results = []
                for item in xs:
                    if item in seen:
                        results.append(item)
                return results
        """,
        expected="O(n^2)",
        justification="Each of the n membership tests scans the list it checks against.",
    ),
    Snippet(
        name="sorted_copy",
        code="""
            def f(xs):
                return sorted(xs)
        """,
        expected="O(n log n)",
        justification="A comparison sort performs theta(n log n) comparisons.",
    ),
    Snippet(
        name="sort_per_element",
        code="""
            def f(xs):
                results = []
                for _ in xs:
                    results.append(sorted(xs))
                return results
        """,
        expected="O(n^2 log n)",
        justification="The n iterations each run an n log n sort.",
    ),
)


def total_copies(n: int) -> int:
    """Count element copies while growing an empty list to `n` appends.

    Args:
        n: number of appends; 0 gives 0.

    Returns:
        Total elements moved by capacity doubling (1 -> 2 -> 4 -> ...).
    """
    copies = 0
    capacity = 1
    length = 0
    for _ in range(n):
        if length == capacity:
            copies += capacity
            capacity *= 2
        length += 1
    return copies


def justify_append_amortization() -> str:
    """Return the one-line argument that `list.append` is amortized O(1)."""
    return (
        "Capacity doubles on overflow, so n appends copy at most 1 + 2 + 4 + ... "
        "<= 2n elements in total — a constant average per append, which is "
        "amortized O(1)."
    )


def main() -> None:
    """Run a few checks. Every solution must pass these before you mark it done."""
    # Grade the ten snippets: the day's completion criterion is 10/10.
    score = 0
    for snippet in SNIPPETS:
        actual = classify(snippet.code)
        assert actual == snippet.expected, (
            f"{snippet.name}: expected {snippet.expected}, got {actual}"
        )
        assert snippet.justification and "\n" not in snippet.justification
        assert snippet.justification.endswith(".")
        score += 1
    assert score == 10, f"graded {score}/10 snippets"

    # Hash membership stays linear where list membership would not
    assert (
        classify(
            """
            def f(xs):
                return [x for x in xs if x in {1, 2, 3}]
            """
        )
        == "O(n)"
    )

    # Unknown calls fail loudly instead of guessing
    try:
        classify("def f(xs):\n    return mystery(xs)")
    except ValueError:
        pass
    else:
        raise AssertionError("unknown calls must be rejected")
    try:
        classify("x = 1")
    except ValueError:
        pass
    else:
        raise AssertionError("a snippet without a function must be rejected")

    # Amortization: total copies never exceed 2n, average stays under 2
    assert total_copies(0) == 0
    assert total_copies(1) == 0          # first allocation copies nothing
    assert total_copies(5) == 7          # copies 1 + 2 + 4 growing 1->2->4->8
    for n in (2, 3, 4, 5, 8, 9, 1000, 4096, 10_000):
        assert total_copies(n) <= 2 * n, n
    assert total_copies(10_000) / 10_000 <= 2
    assert justify_append_amortization().endswith("amortized O(1).")

    print("All tests passed.")


if __name__ == "__main__":
    main()
