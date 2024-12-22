def main():
    # Initialize an empty set to track unique words
    unique_words = set()

    while True:
        # Ask the user to input a word
        word = input("Enter a word: ").strip()

        # Check if the word is already in the set (case-sensitive)
        if word in unique_words:
            # If duplicate is found, print the count of unique words and exit
            print(f"You typed in {len(unique_words)} unique words.")
            break
        else:
            # Add the word to the set of unique words
            unique_words.add(word)

if __name__ == "__main__":
    main()
