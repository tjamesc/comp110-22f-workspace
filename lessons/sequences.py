"""Examples of tuple and range sequences."""


Player = tuple[str, int]
goat: Player = ("MJ", 23)
unc_goat: Player = ("Manek", 35)


for entry in goat:
    print(entry)
len(goat)

# you can't alter a tuple in any way; the following get an error:
# goat[0] = "Me"
# goat.append("Me")

# if you did want to update a tuple, you need to reassign the values altogether
unc_goat = ("Bacot", unc_goat[1] - 30)

# printing a tuple produces its literal syntax
print(goat)

#to print both items on the same line
print(f"{goat[0]}, {goat[1]}")



# now to look at some ranges
zero_to_nine: range = range(0, 10)
print(zero_to_nine)
# just prints out the range, like a list


evens_to_eighty: range = range(0, 81, 2)
print(evens_to_eighty)

for i in evens_to_eighty:
    print(i)


names = list[str] = ["Kris, Lapushin, Scott, Mireya", "Billy"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")

for i in range(0, len(names), 2):
    print(f"{i}. {names[i]}")