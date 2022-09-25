"""Examples of list utilities and unit testing."""

__author__ = "730510525"


def only_evens(nums: list[int]) -> list[int]:
    """Given a list of integers, returns a new list with all elements that are even numbers."""
    i: int = 0
    evens: list[int] = []
    while i < len(nums):
        if nums[i] % 2 == 0:
            evens.append(nums[i])
        i += 1
    return evens


def concat(a_list: list[int], b_list: list[int]) -> list[int]:
    """Concatenates two lists of integers into a single list."""
    full_list: list[int] = []
    i: int = 0
    j: int = 0
    while i < len(a_list):
        full_list.append(a_list[i])
        i += 1
    while j < len(b_list):
        full_list.append(b_list[j])
        j += 1
    return full_list


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Given a full list with start and end indicies, return a new list with the elements between those indicies."""
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    # if len(a_list) == 0:
    #     return a_list
    short_list: list[int] = []
    while start < end:
        short_list.append(a_list[start])
        start += 1
    return short_list