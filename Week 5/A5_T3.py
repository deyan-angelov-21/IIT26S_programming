def askName():
    return input("Insert name: ")

def greetUser(PName):
    print(f"Hello {PName}!")

def main():
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")

if __name__ == "__main__":
    main()