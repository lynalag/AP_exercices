word = input("Type a word to check if it's a palindrome: ")
is_palindrome = True  
length = len(word)


for i in range(length // 2):
    if word[i] != word[-(i + 1)]:  # Compare characters from start and end
        is_palindrome = False
        break  # No need to continue if mismatch found

# Step 3: Output the Result
if is_palindrome:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
