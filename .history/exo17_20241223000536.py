
numbers = []
shoe_sizes = []


numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)


for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)


print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)


numbers.append(3)
numbers.append(5)


numbers = list(set(numbers))  
combined_list = numbers + shoe_sizes


print("Numbers List (after removing duplicates):", numbers)
print("Combined List:", combined_list)
