word = ""
print("program starting.")

while True:
    print("options:")
    print("1 - insert word")
    print("2 - show current word")
    print("3 - show current word in reverse")
    print("0 - exit")
    
    choice = input("your choice: ")
    
    if choice == "1":
        word = input("insert word: ")
    elif choice == "2":
        print(f'current word: "{word}"')
    elif choice == "3":
        print(f'word reversed: "{word[::-1]}"')
    elif choice == "0":
        print("exiting program.")
        break
    else:
        print("unknown option")

print("program ending.")