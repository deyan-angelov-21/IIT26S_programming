correct_password = "triangle"
for i in range(3):
    guess = input("Enter password: ")
    if guess == correct_password:
        print("You logged in successfully!")
        break
    print("Incorrect password.")
else:
    print("Too many failed attempts")