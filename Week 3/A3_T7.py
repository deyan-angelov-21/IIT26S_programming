def main():
    print("Program starting.")
    print("Testing decision structures.")
    
    val = int(input("Insert an integer: "))
    
    print("Options:")
    print("1 -- In one multi-branched decision")
    print("2 -- In multiple independent if-statements")
    print("0 -- Exit")
    
    choice = int(input("Your choice: "))
    
    if choice == 1:
        print("Using one multi-branched decision structure.")
        if val >= 400:
            val += 44
        elif val >= 200:
            val += 22
        elif val >= 100:
            val += 11
        print(f"Result is {val}")
    elif choice == 2:
        print("Using multiple independent if-statements.")
        if val >= 400:
            val += 44
        if val >= 200:
            val += 22
        if val >= 100:
            val += 11
        print(f"Result is {val}")
    elif choice == 0:
        print("Exiting...")
    else:
        print("Unknown option.")

    print()
    print("Program ending.")

if __name__ == "__main__":
    main()