def askDimension(PPrompt: str) -> float:
    return float(input(f"Insert {PPrompt}: "))

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    return PWidth * PHeight

print("Program starting.")
Width = askDimension("width")
Height = askDimension("height")
Area = calcRectangleArea(Width, Height)
print("")
print(f"Area is {Area}")
print("Program ending.")