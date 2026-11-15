from pathlib import Path

print("Program starting.")
print("This program can copy a file.")

source = input("Insert source filename: ")
destination = input("Insert destination filename: ")

folder = Path(__file__).parent

print(f"Reading file '{source}' content.")

file = open(folder / source, "r")
content = file.read()
file.close()

print("File content ready in memory.")

print(f"Writing content into file '{destination}'.")

file = open(folder / destination, "w")
file.write(content)
file.close()

print("Copying operation complete.")
print("Program ending.")