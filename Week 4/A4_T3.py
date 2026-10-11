print("Program starting.")

start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))

print("Starting while-loop:")

current = start
output = []

while current <= stop:
    output.append(str(current))
    current += 1

print(".".join(output))

print("Program ending.")