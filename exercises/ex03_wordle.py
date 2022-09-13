"""EX03 - Full wordle game with multiple attempts and functions."""
__author__ = "730510525"


def contains_char(string: str, char: str) -> bool:
    """Searches to see if the second character argument is present in the first string argument."""
    assert len(char) == 1
    j: int = 0
    while j + 1 <= len(string):
        if char == string[j]:
            return True
        else:
            j += 1
    return False
# this function will take future variables as its arguments, when we use this function as an abstraction to test
# if a letter in the wrong spot is present in the secret word at all...it increases the index of the secret word
# until a letter matches the character or the index of the secret word is out of range


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, SECRET: str) -> str:
    """Represents the accuracy of a guess to the secret word with colored emoji boxes."""
    assert len(guess) == len(SECRET)
    box_sequence: str = ""
    i: int = 0
    sec_index: int = 0
    if guess == SECRET:
        box_sequence += GREEN_BOX * len(SECRET)
    else:
        while i < len(SECRET):
            if guess[i] == SECRET[sec_index]:
                box_sequence += GREEN_BOX
            else: 
                contains_char(SECRET, guess[i])
                if contains_char(SECRET, guess[i]):
                    box_sequence += YELLOW_BOX
                else: 
                    box_sequence += WHITE_BOX
            i += 1
            sec_index += 1
    return box_sequence
# creates the box sequences for correct, incorrect, and right letter-wrong spot guesses...to determine whether
# a letter gets a yellow or white box, we use the contains_char function, so we don't need a nested while loop


def input_guess(input_len: int) -> str:
    """Provided an intenger argument, prompts the user to make a guess with the same number of characters as the given integer."""
    response: str = input(f"Enter a {input_len} character word: ")
    while len(response) != input_len:
        response = input(f"That wasn't {input_len} chars! Try again: ")
    return response
# compares the length of the secret word to the length of the guess, so that the user guesses an appropriate number
# of characters every turn...acts as an abstraction for the main function


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    playing: bool = True
    SECRET: str = "codes"
    while turn <= (len(SECRET) + 1) and playing:
        print(f"=== Turn {turn}/6 ===")
        user_guess: str = input_guess(len(SECRET))
        print(emojified(user_guess, SECRET))
        turn += 1
        if emojified(user_guess, SECRET) == GREEN_BOX * len(SECRET):
            print(f"You won in {turn - 1}/6 turns!")
            return None
        elif turn > 6:
            print("X/6 - Sorry, try again tomorrow!")
            return None
# the main function is like a facilitator, it guides where the code control flow goes...it starts in the main function
# when it is called, but passes its own variables as arguments to other functions already created...first moves into
# input_guess to receive a valid guess from the user, which is determined and created into an emoji sequence by
# emojified and contains_char
   

if __name__ == "__main__":
    main()