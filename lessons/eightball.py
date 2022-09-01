from random import randint

question: str = input("What is your yes/no question? ")
response: int = int(randint(0, 3))
#randint creates a random integer in the range given


if response == 0:
    print("Not at all, boi")
elif response == 1:
    print("Ask again later...")
elif response == 2:
    print("Yes, daddy")
else: 
    print("Idk man, I'm a ball")