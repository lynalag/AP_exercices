def anagrams(str1, str2):
    
    if len(str1) != len(str2):
        return False
    
    
    return sorted(str1) == sorted(str2)

# Exemples d'utilisation
print(anagrams("tame", "meta"))
print(anagrams("tame", "mate"))
print(anagrams("tame", "team"))
print(anagrams("tabby", "batty"))  
print(anagrams("python", "java"))  
