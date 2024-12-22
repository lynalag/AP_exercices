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
import math

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

# Fonction pour retourner un dictionnaire avec les statistiques
def list_statistics(lst):
    """
    Retourne un dictionnaire avec les statistiques de la liste.
    
    :param lst: Liste des éléments
    :return: Dictionnaire avec les statistiques de la liste
    """
    stats = {
        "length": length(lst),
        "mean": mean(lst),
        "range": range_of_list(lst),
        "median": median(lst),
        "standard_deviation": standard_deviation(lst)
    }
    return stats

# Test avec une liste d'exemple
numbers = [1, 2, 3, 4, 5]
print("List statistics for numbers:", numbers)
print("Length:", length(numbers))
print("Mean:", mean(numbers))
print("Range:", range_of_list(numbers))
print("Median:", median(numbers))
print("Standard Deviation:", standard_deviation(numbers))

# Exemple d'utilisation avec une liste vide et avec des valeurs négatives ou flottantes
empty_list = []
try:
    print("Length of empty list:", length(empty_list))
except Exception as e:
    print(e)

negative_numbers = [-1, -2, -3, -4, -5]
print("Length of negative numbers list:", length(negative_numbers))
print("Mean of negative numbers:", mean(negative_numbers))
print("Range of negative numbers:", range_of_list(negative_numbers))

float_numbers = [1.5, 2.5, 3.5]
print("Length of float numbers list:", length(float_numbers))
print("Mean of float numbers:", mean(float_numbers))
