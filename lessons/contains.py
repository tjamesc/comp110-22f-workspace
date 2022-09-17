"""Example of a utility list function."""

def contains(needle: str, haystack: list[str]) -> bool:
    """Searches for a string in a list of strings."""
    i: int = 0
    while i < len(haystack):
        if needle == haystack[i]:
            return True
        i += 1
    return False


my_list: list[str] = ["one", "two", "three"]