"""Examples of using lists in a simple game."""
# use command + "/" to comment out any highlighted lines of code

from random import randint

rolls: list[int] = list()


while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

rolls.pop()
print(rolls)

# keeps rolling until 1 is rolled
# second conditional would not on its own, as rolls has no values in the list at the start

# to find the sum of values in a list
i: int = 0
sum: int = 0

while i < len(rolls):
    sum += rolls[i]
    i += 1

print(f"Total score: {sum}")