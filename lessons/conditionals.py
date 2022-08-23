"""Example of conditional if-else statements."""

SECRET: int = 3

print("I'm thinking of a number between 1 and 5...what is it?")
guess: int = int(input("What is your guess? ")) 
#the answer to the str question will be a str unless converted to an int


if guess == SECRET:
    print("CORRECT!!!")
elif guess > SECRET:
    print("Wrong...you guessed too high")
else:
    print("Wrong...you guessed too low")


print("Game over")
