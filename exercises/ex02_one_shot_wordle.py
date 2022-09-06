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
    elif len(guess) != len(SECRET):
        guess = input(f"That was not {len(SECRET)} letters! Try again: ")
    else:
        while i + 1 <= len(SECRET):
            if guess[i] == SECRET[i]:
                box_sequence += GREEN_BOX
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
            i += 1
        print(box_sequence)
        print("Not quite. Play again soon!")
        playing = False