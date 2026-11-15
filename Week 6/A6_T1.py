from pathlib import Path

print("Program starting.")
print("This program can read a file.")

filename = input("Insert filename: ")

filepath = Path(__file__).parent / filename

file = open(filepath, "r")
content = file.read()
file.close()

print(f'#### START "{filename}" ####')
print(content, end="")
print(f'\n#### END "{filename}" ####')

print("Program ending.")