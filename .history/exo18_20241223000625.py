def display_menu():
    print("\nMenu:")
    print("1. Append")
    print("2. Insert")
    print("3. Pop")
    print("4. Remove")
    print("5. Quit")

def main():
    # Initialize the list
    numbers = [1, 2, 3, 4, 5]
    
    print("Initial List:", numbers)

    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            # Append an element
            try:
                value = int(input("Enter value to append: "))
                numbers.append(value)
                print("Updated List:", numbers)
            except ValueError:
                print("Invalid value. Please enter an integer.")

        elif choice == 2:
            # Insert an element at a specific position
            try:
                value = int(input("Enter value to insert: "))
                index = int(input("Enter index: "))
                if index < 0 or index > len(numbers):
                    print("Index out of range.")
                else:
                    numbers.insert(index, value)
                    print("Updated List:", numbers)
            except ValueError:
                print("Invalid input. Please enter integers for value and index.")

        elif choice == 3:
            # Pop an element
            try:
                if numbers:
                    popped_value = numbers.pop()
                    print(f"Popped value: {popped_value}")
                    print("Updated List:", numbers)
                else:
                    print("The list is empty. Cannot pop.")
            except IndexError:
                print("Error: List is empty, cannot pop.")

        elif choice == 4:
            # Remove an element
            try:
                value = int(input("Enter value to remove: "))
                if value in numbers:
                    numbers.remove(value)
                    print("Updated List:", numbers)
                else:
                    print(f"Value {value} not found in the list.")
            except ValueError:
                print("Invalid value. Please enter an integer.")

        elif choice == 5:
            # Quit the program
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
