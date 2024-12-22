
user_list = []

while True:
    
    user_input = input("Enter a number: ")
    
    
    if user_input.isdigit(): 
        number = int(user_input)
        
       
        if number == 0:
            break
        
        
        user_list.append(number)
        
        # Afficher la liste actuelle et la liste triée
        print(f"Current List: {user_list}")
        print(f"Sorted List: {sorted(user_list)}")
    else:
        print("Please enter a valid integer.")
        
print("Program terminated.")
