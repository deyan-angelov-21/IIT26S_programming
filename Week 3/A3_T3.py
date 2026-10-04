name = input("Before the menu, please insert your name: ")

print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")

print("\nOptions:")
print("1 -- Print welcome message")
print("2 -- Exit")

choice = input("Your choice: ")

if choice == "1":
    print(f"Welcome {name}!")
elif choice == "2":
    print("Exiting...")
else:
    print("Unknown option.")

print("Program ending.")