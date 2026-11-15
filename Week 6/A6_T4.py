from pathlib import Path

print("Program starting.")
print("This program analyses a list of names from a file.")

filename = input("Insert filename to read: ")

folder = Path(__file__).parent

print(f"Reading names from '{filename}'.")
print("Analysing names...")

file = open(folder / filename, "r")
names = []

for line in file:
    line = line.strip()
    parts = line.split(";")

    for name in parts:
        name = name.strip()
        if name != "":
            names.append(name)

file.close()

amount = len(names)
shortest = min(names, key=len)
longest = max(names, key=len)

total = 0
for name in names:
    total += len(name)

average = total / amount

print("Analysis complete!")
print("#### REPORT BEGIN ####")
print(f"Name count: {amount}")
print(f"Shortest name: {len(shortest)} chars")
print(f"Longest name: {len(longest)} chars")
print(f"Average name: {average:.2f} chars")
print("#### REPORT END ####")
print("Program ending.")