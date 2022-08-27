"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730510525"


guessed_word: str = input("Enter a 5-character word: ")
if len(guessed_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

guessed_letter: str = input("Enter a single character: ")
if len(guessed_letter) != 1:
    print("Error: Character must be a single character.")
    exit()


print("Searching for " + guessed_letter + " in " + guessed_word)
quantity: int = 0


if guessed_letter == guessed_word[0]:
    print(guessed_letter + " found at index 0")
    quantity += 1

if guessed_letter == guessed_word[1]:
    print(guessed_letter + " found at index 1")
    quantity += 1

if guessed_letter == guessed_word[2]:
    print(guessed_letter + " found at index 2")
    quantity += 1

if guessed_letter == guessed_word[3]:
    print(guessed_letter + " found at index 3")
    quantity += 1
                
if guessed_letter == guessed_word[4]:
    print(guessed_letter + " found at index 4")
    quantity += 1


if quantity == 0:
    print("No instances of " + guessed_letter + " found in " + guessed_word)
else:
    if quantity == 1:
        print("1 instance of " + guessed_letter + " found in " + guessed_word)
    else:
        print(str(quantity) + " instances of " + guessed_letter + " found in " + guessed_word)
