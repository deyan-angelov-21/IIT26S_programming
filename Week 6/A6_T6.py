LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def askRows() -> str:
    rows = [] # initializing a list to store the rows 
    while True:
        row = input("Insert row(empty stops):")
        if row == "":
            break
        rows.append(row)
    print("In the row string function.")
    return ("\n".join(rows)) 

def shiftCharacters(Character:str, Alphabet:str, Shift:int) -> str:
    if Character in Alphabet:
        Index = Alphabet.index(Character)
        shifted_index = (Index + Shift) % len(Alphabet)
        return Alphabet[shifted_index]
    return Character

def roll(Content: str) -> str:
    NewContent = ""
    Shift = 13
    for Character in Content:
        if Character in LOWER_ALPHABETS:
            NewContent += shiftCharacters(Character, LOWER_ALPHABETS, Shift)
        elif Character in UPPER_ALPHABETS:
            NewContent += shiftCharacters(Character, UPPER_ALPHABETS, Shift)
        else:
            NewContent += Character
    return NewContent

def writefile(filename, Content) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(Content)
        file.close()

def main() -> None:
    print("Program starting.")
    print("Collecting plain text rows for ciphering.")
    Rows = askRows()
    print("#### Ciphered text ####")
    CipheredText = roll(Rows)
    print(CipheredText)
    print("#### Ciphered text ####")
    filename = input("Insert filename to save: ")
    writefile(filename, CipheredText)
    print("Ciphered text saved!")
    print("Program ending.")
    return None
main()