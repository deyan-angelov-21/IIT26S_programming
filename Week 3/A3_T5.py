def main():
    print("Program starting.")
    print()
    print("Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    
    choice = input("Your choice: ")
    
    if choice == "1":
        temp = float(input("Insert the amount of Celsius: "))
        converted = temp * 1.8 + 32
        print(f"{temp:.1f} °C equals to {converted:.1f} °F")
    elif choice == "2":
        temp = float(input("Insert the amount of Fahrenheit: "))
        converted = (temp - 32) / 1.8
        print(f"{temp:.1f} °F equals to {converted:.1f} °C")
    elif choice == "3" or choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")
        
    print()
    print("Program ending.")

if __name__ == "__main__":
    main()