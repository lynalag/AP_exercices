def anagrams(str1, str2):
   
    if len(str1) != len(str2):
        return False
    
    
    return sorted(str1) == sorted(str2)


word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")


if anagrams(word1, word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")
