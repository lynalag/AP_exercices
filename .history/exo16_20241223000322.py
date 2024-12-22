
numbers = [1, 2, 3, 4, 5]

while True:
    
    try:
        index = int(input("Enter index (-1 to quit): "))
    except ValueError:
        print("Invalid input. Please enter an integer for the index.")
        continue

    
    if index == -1:
        break

    
    if index < 0 or index >= len(numbers):
        print("Index out of range. Please try again.")
        continue

    
    try:
        new_value = int(input("Enter new value: "))
    except ValueError:
        print("Invalid input. Please enter an integer for the new value.")
        continue

    # Update the list
    numbers[index] = new_value
    print(numbers)
