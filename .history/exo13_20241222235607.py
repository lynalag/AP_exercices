while True:
    
    user_input = input("Please type in a string: ")
    
   
    if user_input == "":
        break
    
    # Print the string and its underline
    print(user_input)
    print("-" * len(user_input))
