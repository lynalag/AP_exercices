# Input: Ask the user for a string
user_input = input("Please type in a string: ")

# List of vowels to check
vowels = ['a', 'e', 'o']

# Check for each vowel and print the result
for vowel in vowels:
    if vowel in user_input:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
#Please type in a string: lyna
#a found
#e not found
#o not found