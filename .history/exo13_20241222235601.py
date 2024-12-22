while True:
    # Ask the user for a string
    user_input = input("Please type in a string: ")
    
    # Check if the input is empty to exit the loop
    if user_input == "":
        break
    
    # Print the string and its underline
    print(user_input)
    print("-" * len(user_input))
