"""Tests for utils functions for ex05."""

__author__ = "730510525"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_only_evens() -> None:
    """Test function for only_evens."""
    nums: list[int] = [4, 11, 3, -14, 55, 8, 90, 25, 0]
    assert only_evens(nums) == [4, -14, 8, 90, 0]


def test_only_evens_none() -> None:
    """Test function for only_evens, where no items in the list are even."""
    nums: list[int] = [41, 3, 29]
    assert only_evens(nums) == []


def test_only_evens_empty() -> None:
    """Test function for only_evens, where the list is empty."""
    nums: list[int] = []
    assert only_evens(nums) == []


def test_concat() -> None:
    """Test for concat function."""
    a_list: list[int] = [111, 2, 3, -5, 0]
    b_list: list[int] = [47, -99, 22]
    assert concat(a_list, b_list) == [111, 2, 3, -5, 0, 47, -99, 22]


def test_concat_one_empty() -> None:
    """Test for concat function, where one list is empty."""
    a_list: list[int] = []
    b_list: list[int] = [-1, 0, 200]
    assert concat(a_list, b_list) == [-1, 0, 200]


def test_concat_both_empty() -> None:
    """Test for concat function, where both lists are empty."""
    a_list: list[int] = []
    b_list: list[int] = []
    assert concat(a_list, b_list) == []


def test_sub() -> None:
    """Test for sub function."""
    a_list: list[int] = [1, -3, 0, 44, 18, -71]
    start: int = 0
    end: int = 3
    assert sub(a_list, start, end) == [1, -3, 0]


def test_sub_diff_bounds() -> None:
    """Test for sub function with invalid bounds."""
    a_list: list[int] = [1, 22, -4, 18]
    start: int = -3
    end: int = 40
    assert sub(a_list, start, end) == [1, 22, -4, 18]


def test_sub_empty() -> None:
    """Test for sub function, where the list is empty."""
    a_list: list[int] = []
    start: int = 1
    end: int = 4
    assert sub(a_list, start, end) == []