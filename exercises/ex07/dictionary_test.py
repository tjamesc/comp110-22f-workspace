"""Unit tests for EX07."""

__author__ = "730510525"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count
import pytest


def test_invert() -> None:
    """Test for invert function."""
    original: dict[str, str] = {"Walter": "White", "Jesse": "Pinkman", "Hank": "Schrader"}
    assert invert(original) == {"White": "Walter", "Pinkman": "Jesse", "Schrader": "Hank"}


def test_invert_one_key() -> None:
    """Test for invert function with only one key."""
    original: dict[str, str] = {"Walter": "White"}
    assert invert(original) == {"White": "Walter"}


def test_invert_dup_key() -> None:
    """Test for invert function with a duplicate key."""
    with pytest.raises(KeyError):
        original: dict[str, str] = {"Walter": "White", "Jesse": "Pinkman", "Hank": "Schrader", "Skylar": "White"}
        invert(original)


def test_favorite_color() -> None:
    """Test for favorite_color function."""
    colors: dict[str, str] = {"Tom": "blue", "Madi": "blue", "Andre": "red", "Lucas": "green"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_one_entry() -> None:
    """Test for favorite_color function, with only one entry."""
    colors: dict[str, str] = {"Tom": "blue"}
    assert favorite_color(colors) == "blue"


def test_favorite_color_tie() -> None:
    """Test for favorite_color function, where there is a tie for most frequent color."""
    colors: dict[str, str] = {"Tom": "blue", "Madi": "blue", "Andre": "red", "Lucas": "green", "Emily": "green"}
    assert favorite_color(colors) == "blue"


def test_count() -> None:
    """Test for count function."""
    input_list: list[str] = ["wow", "wow", "woah", "wow", "woah"]
    assert count(input_list) == {"wow": 3, "woah": 2}


def test_count_common_key() -> None:
    """Test for count function, with only one common key."""
    input_list: list[str] = ["wow", "wow", "wow", "wow", "wow"]
    assert count(input_list) == {"wow": 5}


def test_count_empty() -> None:
    """Test for count function, with no entries in the original list."""
    input_list: list[str] = []
    assert count(input_list) == {}