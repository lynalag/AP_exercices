# Demander à l'utilisateur de saisir un entier positif N
while True:
    try:
        N = int(input("Please enter a positive integer N: "))
        if N > 0:
            break
        else:
            print("Please enter a positive integer greater than 0.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Afficher les nombres de -N à N (excluant 0)
for i in range(-N, N + 1):
    if i != 0:
        print(i)
