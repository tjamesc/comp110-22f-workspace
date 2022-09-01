"""Another use of while loops to iterate through a collection."""

user_string: str = input("Give me a string! ")

#the variable i is a common counter varibale name in programming (i is short for iterator)
i: int = 0

while i < len(user_string):
    print(user_string[i])
    i += 1

print("Done!")