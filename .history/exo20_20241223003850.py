
user_list = []

while True:
    
    user_input = input("Enter a number: ")
    
    # Vérifier si l'entrée est un nombre entier
    if user_input.isdigit():  # Vérifie si l'entrée est un nombre entier
        number = int(user_input)
        
        # Si l'utilisateur entre 0, arrêter la boucle
        if number == 0:
            break
        
        # Ajouter le nombre à la liste
        user_list.append(number)
        
        # Afficher la liste actuelle et la liste triée
        print(f"Current List: {user_list}")
        print(f"Sorted List: {sorted(user_list)}")
    else:
        print("Please enter a valid integer.")
        
print("Program terminated.")
