def anagrams(str1, str2):
    # Vérifier si les deux chaînes ont la même longueur
    if len(str1) != len(str2):
        return False
    
    # Trier les deux chaînes et comparer
    return sorted(str1) == sorted(str2)

# Demander à l'utilisateur de saisir deux mots
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Vérifier si les mots sont des anagrammes
if anagrams(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")
