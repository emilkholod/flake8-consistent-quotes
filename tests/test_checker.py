import ast

import pytest
from tests.utils import get_absolute_path

from flake8_consistent_quotes.checker import Flake8ConsistentQuotesChecker


def run_checker(filename: str) -> list[tuple[int, int, str]]:
    """Запускаем чекер на переданном коде"""
    with open(get_absolute_path(filename)) as f:
        code = f.read()
    tree = ast.parse(code)
    checker = Flake8ConsistentQuotesChecker(tree, get_absolute_path(filename))
    return list(checker.run())  # type: ignore[no-untyped-call]


@pytest.mark.parametrize(
    "filename",
    [
        "data/pass_double_quotes.py",
        "data/pass_file_without_quotes.py",
        "data/pass_function_docstring.py",
        "data/pass_function_without_docstring.py",
        "data/pass_module_docstring.py",
        "data/pass_single_quotes.py",
        "data/pass_variable_docstring.py",
        "data/pass_wrapped_string.py",
    ],
)
def test_consistent_quotes(filename):
    errors = run_checker(filename)
    assert errors == []


def test_inconsistent_quotes():
    filename = "data/failure_incosistent_quotes.py"
    errors = run_checker(filename)
    assert errors
