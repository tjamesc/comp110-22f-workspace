"""Practice with functions."""


def love(subject: str) -> str:
    """Given a subject as a parameter, returns a loving string."""
    return f"I love you, {subject}!"

# to use the function in the REPL, use the line "from lessons.module_name import function_name"


def spread_love(to: str, n: int) -> str:
    """Generates a str repeating a loving message n times"""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note

# \n creates a new line for the print statements, each time a statement is made with the love function, a new line is created
# must assign the variables, locally--within the function and only applying to the function--or else they will end up in the globals section

subject: str = input("Who do you love? ")
print(spread_love(subject, 10))
