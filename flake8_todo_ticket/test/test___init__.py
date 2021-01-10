from typing import List

from flake8_todo_ticket import Flake8Result
from flake8_todo_ticket import check as _check

T400 = "T400 Badly formatted TODO. Use TODO(name)[ticket_number]"  # noqa: T400


def check(line: str) -> List[Flake8Result]:
    """Check, but return a list not an iterator"""
    return list(_check(line))


def test_todo_ticket() -> None:
    assert check("# TODO in comment") == [(2, T400)]  # noqa: T400
    assert check("# FIXME") == []
    assert check("TODO") == [(0, T400)]  # noqa: T400


def test_todo_word_boundaries() -> None:
    assert check("# MASTODON") == []
    assert check("#TODO") == [(1, T400)]  # noqa: T400


def test_todo_ticket_multiple() -> None:
    assert check("# TODO(tom)[001] with a TODO") == [(24, T400)]  # noqa: T400
    assert check("# TODO with a TODO") == [(2, T400), (14, T400)]  # noqa: T400
