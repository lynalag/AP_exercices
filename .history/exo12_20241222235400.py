# Input: Ask the user for the width and height of the rectangle
width = int(input("Width: "))
height = int(input("Height: "))

# Output: Print the rectangle of hash characters
for _ in range(height):
    print("#" * width)
