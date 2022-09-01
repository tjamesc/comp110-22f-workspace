"""Example of a while loop."""


counter: int = 0
maximum: int = int(input("What should I count to? "))

while counter < maximum + 1:
    counter_sqrt: int = round(counter ** 0.5, 2)
    print("The square root of " + str(counter) + " is " + str(counter_sqrt))
    counter += 1

print("Done!")