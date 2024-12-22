import math

# Fonction pour calculer la longueur de la liste
def length(lst):
    """
    Retourne le nombre d'éléments dans la liste.
    
    :param lst: Liste des éléments
    :return: Nombre d'éléments dans la liste
    """
    if not isinstance(lst, list):
        raise TypeError("L'entrée doit être une liste.")
    return len(lst)

# Fonction pour calculer la moyenne de la liste
def mean(lst):
    """
    Calcule la moyenne (moyenne arithmétique) de la liste.
    
    :param lst: Liste des éléments
    :return: Moyenne des éléments de la liste
    """
    if not isinstance(lst, list):
        raise TypeError("L'entrée doit être une liste.")
    
    if len(lst) == 0:
        raise ValueError("La liste ne peut pas être vide.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Tous les éléments de la liste doivent être des nombres.")
    
    return sum(lst) / len(lst)

# Fonction pour calculer l'étendue (différence entre le max et le min) de la liste
def range_of_list(lst):
    """
    Retourne la différence entre la valeur maximale et minimale de la liste.
    
    :param lst: Liste des éléments
    :return: Différence entre max et min dans la liste
    """
    if not isinstance(lst, list):
        raise TypeError("L'entrée doit être une liste.")
    
    if len(lst) == 0:
        raise ValueError("La liste ne peut pas être vide.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Tous les éléments de la liste doivent être des nombres.")
    
    return max(lst) - min(lst)

# Fonction pour calculer la médiane (Bonus)
def median(lst):
    """
    Calcule la médiane de la liste.
    
    :param lst: Liste des éléments
    :return: Médiane des éléments de la liste
    """
    if not isinstance(lst, list):
        raise TypeError("L'entrée doit être une liste.")
    
    if len(lst) == 0:
        raise ValueError("La liste ne peut pas être vide.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Tous les éléments de la liste doivent être des nombres.")
    
    lst_sorted = sorted(lst)
    n = len(lst_sorted)
    
    if n % 2 == 1:
        return lst_sorted[n // 2]
    else:
        return (lst_sorted[(n // 2) - 1] + lst_sorted[n // 2]) / 2

# Fonction pour calculer l'écart-type (Bonus)
def standard_deviation(lst):
    """
    Calcule l'écart-type des éléments de la liste.
    
    :param lst: Liste des éléments
    :return: Écart-type des éléments de la liste
    """
    if not isinstance(lst, list):
        raise TypeError("L'entrée doit être une liste.")
    
    if len(lst) == 0:
        raise ValueError("La liste ne peut pas être vide.")
    
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Tous les éléments de la liste doivent être des nombres.")
    
    mean_val = mean(lst)
    squared_differences = [(x - mean_val) ** 2 for x in lst]
    return math.sqrt(sum(squared_differences) / len(lst))

# Demander à l'utilisateur d'entrer une liste de nombres
def get_user_list():
    user_list = []
    print("Veuillez entrer des nombres (entrez 'done' pour arrêter) :")
    
    while True:
        user_input = input("Entrez un nombre: ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            user_list.append(number)
        except ValueError:
            print("Ce n'est pas un nombre valide, essayez encore.")
    
    return user_list

# Fonction principale
def main():
    user_list = get_user_list()
    
    if len(user_list) == 0:
        print("La liste est vide, veuillez entrer des nombres.")
        return
    
    print("\nStatistiques de la liste:")
    print("Longueur de la liste:", length(user_list))
    print("Moyenne de la liste:", mean(user_list))
    print("Étendue de la liste:", range_of_list(user_list))
    print("Médiane de la liste:", median(user_list))
    print("Écart-type de la liste:", standard_deviation(user_list))

# Lancer le programme
if __name__ == "__main__":
    main()
