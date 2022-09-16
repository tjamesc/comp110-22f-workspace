"""Practice with useful functions for lists."""
__author__ = "730510525"


def all(num_list: list[int], num: int) -> bool:
    """Searches a list of integers to see if all entries in the list are equal to a specified number."""
    i: int = 0
    if len(num_list) == 0:
        return False
    while i < len(num_list):
        if num == num_list[i]:
            i += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Displays the maximum value out of a list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    largest: int = input[i]
    while i < len(input):
        if input[i] > largest:
            largest = input[i]
        i += 1
    return largest


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Tests if two lists are exactly indentical, having the same integer at each index."""
    i: int = 0
    if len(list_1) != len(list_2):
        return False
    while i < len(list_1):
        if list_1[i] != list_2[i]:
            return False
        i += 1
    return True


# def main() -> None:
#     """Main function to evaluate some properties of lists."""
#     list_1: list[int] = [1, 30, 55, 4, 14, 88]
#     list_2: list[int] = [1, 30, 55, 4, 14, 89]
#     list_3: list[int] = [2, 2, 2, 2]
#     num: int = 2
#     maximum: int = max(list_1)
#     all_same: bool = all(list_3, num)
#     equality: bool = is_equal(list_1, list_2)
#     print(f"The maximum value in list 1 is {maximum}!")
#     if all_same:
#         print(f"All values in list 3 are all {num}!")
#     else:
#         print(f"Not all of the values in list 3 are equal to {num}")
#     if equality:
#         print("List 1 and list 2 are identical!")
#     else:
#         print("List 1 and list 2 are different.")


# if __name__ == "__main__":
#     main()