"""One-shot wordle exercise for COMP 110."""

__author__ = "730510525"


SECRET: str = "python"
playing: bool = True
guess: str = input(f"What is your {len(SECRET)} letter guess? ")


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


i: int = 0
box_sequence: str = ""


while playing:
    if guess == SECRET:
        box_sequence = GREEN_BOX * len(SECRET)
        print(box_sequence)
        print("Woo! You got it!")
        playing = False
# ends the game and displays all green boxes if the user guesses correctly
    elif len(guess) != len(SECRET):
        guess = input(f"That was not {len(SECRET)} letters! Try again: ")
# if the guess has an incorrect length, the user will be prompted for a new input until a valid guess is given
    else:
        while i + 1 <= len(SECRET):
            if guess[i] == SECRET[i]:
                box_sequence += GREEN_BOX
# if the guess is valid but incorrect, we enter this if-statement, giving green boxes for correct letter guesses
            else:
                letter_present: bool = False
                j: int = 0
                search: bool = True
                while j + 1 <= len(SECRET) and search:
                    if guess[i] == SECRET[j]:
                        search = False
                        letter_present = True
                    else:
                        j += 1
                if letter_present:
                    box_sequence += YELLOW_BOX
                else:
                    box_sequence += WHITE_BOX
# the else block of the aforementioned if-statement contains the code to determine whether or
# not a letter is present in the word, even if it's in the wrong spot, using a comparison search, where
# the index of the secret is changed and the guessed letter index is constant until all spots are checked
            i += 1
        print(box_sequence)
        print("Not quite. Play again soon!")
        playing = False
# the playing = False statements ensure the while loop stops running when the game is over