print("Program starting.")

number = int(input("Insert a positive integer: "))

steps = 0
sequence = str(number)
while number != 1:
    if number % 2 == 0:
        number //= 2
    else:
        number = 3 * number + 1
    sequence += f" -> {number}"
    steps += 1

print(sequence)
print(f"Sequence had {steps} total steps.")
print()
print("Program ending.")