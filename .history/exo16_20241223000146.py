# Initialize the list
numbers = [1, 2, 3, 4, 5]

while True:
    # Ask the user for an index
    try:
        index = int(input("Enter index (-1 to quit): "))
    except ValueError:
        print("Invalid input. Please enter an integer for the index.")
        continue

    # Exit condition
    if index == -1:
        break

    # Check for valid index range
    if index < 0 or index >= len(numbers):
        print("Index out of range. Please try again.")
        continue

    # Ask for a new value
    try:
        new_value = int(input("Enter new value: "))
    except ValueError:
        print("Invalid input. Please enter an integer for the new value.")
        continue

    # Update the list
    numbers[index] = new_value
    print(numbers)
