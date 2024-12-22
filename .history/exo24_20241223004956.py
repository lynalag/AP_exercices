def anagrams(str1, str2):
    # Vérifier si les deux chaînes ont la même longueur
    if len(str1) != len(str2):
        return False
    
    # Trier les deux chaînes et comparer
    return sorted(str1) == sorted(str2)

# Exemples d'utilisation
print(anagrams("tame", "meta"))  # True
print(anagrams("tame", "mate"))  # True
print(anagrams("tame", "team"))  # True
print(anagrams("tabby", "batty"))  # False
print(anagrams("python", "java"))  # False
