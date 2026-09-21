print("Program starting.")

name = input("What is your name: ")
first_number = float(input("Enter a floating point number: "))    
second_number = float(input("Enter second floating point number: "))
float_final = first_number * second_number

print(f"{name} you gave numbers {first_number} and {second_number}.")
print(f"Multiplying the first and second number will result in product {round(float_final, 2)}")

print("Program ending.")