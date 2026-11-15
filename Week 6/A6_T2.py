print("Program starting.")

firstname = input("Insert first name: ")
lastname = input("Insert last name: ")
filename = input("Insert filename: ")

file = open(filename, "w")
file.write(firstname + "\n")
file.write(lastname + "\n")
file.write("\n")
file.close()

print("Program ending.")