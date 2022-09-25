"""Tests for the sum function."""

from lessons.sum import sum


# these first two tests are EDGE CASES (not very useful but formalities to check the rare, iffy cases)
def test_sum_empty() -> None:
    xs: list[float] = []
    assert sum(xs) == 0.0


def test_sum_single() -> None:
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0


# the next is a USE CASE (actaul tests we would want to run)
def test_sum_many() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0
