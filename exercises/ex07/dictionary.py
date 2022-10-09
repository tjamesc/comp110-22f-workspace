"""EX07--Dictionary Functions."""

__author__ = "730510525"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    inverted: dict[str, str] = {}
    for key in original:
        inverted[original[key]] = key
    if len(original) != len(inverted):
        raise KeyError
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the color that appears as a value most frequently in the list."""
    color_list: list[str] = []
    for key in colors:
        color_list.insert(0, colors[key])
    color_freq: dict[str, int] = count(color_list)
    inverted: dict[int, str] = {}
    for color in color_freq:
        inverted[color_freq[color]] = color
    frequencies: list[int] = []
    for item in inverted:
        frequencies.append(item)
    most_freq: int = max(frequencies)
    return inverted[most_freq]


def count(input_list: list[str]) -> dict[str, int]:
    """Returns a dictionary with the frequency distribution for each item in the input list."""
    output: dict[str, int] = {}
    counter: int = 1
    for item in input_list:
        if item in output:
            output[item] += 1
        else:
            output[item] = 1
    return output