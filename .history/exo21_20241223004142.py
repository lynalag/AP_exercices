
def length(lst):
    """
    Retourne le nombre d'éléments dans la liste.
    
    :param lst: Liste des éléments
    :return: Nombre d'éléments dans la liste
    """
    if not isinstance(lst, list):
        raise TypeError("L'entrée doit être une liste.")
    return len(lst)


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


