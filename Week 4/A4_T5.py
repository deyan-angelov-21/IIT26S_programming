print("Program starting.")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))

error_found = False

if start >= stop:
    print("Starting point value must be less than stopping point value.")
    error_found = True

if not (start <= inspection <= stop):
    print("Inspection value must be within the range of start and stop.")
    error_found = True

if not error_found:
    print("First loop - inspection with break:")
    first_output = []
    for i in range(start, stop + 1):
        if i == inspection:
            break
        first_output.append(str(i))
    print(".".join(first_output))

    print("Second loop - inspection with continue:")
    second_output = []
    for i in range(start, stop + 1):
        if i == inspection:
            continue
        second_output.append(str(i))
    print(".".join(second_output))

print("Program ending.")
