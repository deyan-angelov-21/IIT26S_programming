print("Program starting.")

words_count = 0
chars_count = 0

while True:
    word = input("Insert word (empty stops): ")
    if word == "":
        break
    words_count += 1
    chars_count += len(word)

print("You inserted:")
print(f"- {words_count} words")
print(f"- {chars_count} characters")

print("Program ending.")