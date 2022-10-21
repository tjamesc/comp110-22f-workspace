"""Example of for loop syntax."""

names: list[str] = ["Tom", "Madi", "Andre", "Lucas"]

print("while output...")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1


print("for output...")
for name in names:
    print(name)