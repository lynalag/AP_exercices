
numbers = []
shoe_sizes = []


numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

# Add items to the shoe_sizes list using a loop
for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)

# Print the lists with descriptive labels
print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)

# Bonus: Add duplicate values to numbers
numbers.append(3)
numbers.append(5)

# Handle duplicates by removing them (optional step)
numbers = list(set(numbers))  # This converts to a set and back to a list to remove duplicates

# Bonus: Create a third list combining numbers and shoe_sizes
combined_list = numbers + shoe_sizes

# Print results of bonus tasks
print("Numbers List (after removing duplicates):", numbers)
print("Combined List:", combined_list)
