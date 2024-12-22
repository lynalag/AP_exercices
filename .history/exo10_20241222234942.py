word = input("Type a word to check if it's a palindrome: ")
is_palindrome = True  
length = len(word)


for i in range(length // 2):
    if word[i] != word[-(i + 1)]:  
        is_palindrome = False
        break 


if is_palindrome:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
