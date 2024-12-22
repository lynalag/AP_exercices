def main():
    
    unique_words = set()
    total_words = 0

    while True:
        # Ask the user to input a word (case insensitive)
        word = input("Enter a word: ").strip()

        # Convert the word to lowercase for case-insensitive comparison
        word_lower = word.lower()

        # Check if the word is a duplicate (case-insensitive)
        if word_lower in unique_words:
            # If duplicate is found, print the count of unique words and exit
            print(f"You typed in {len(unique_words)} unique words.")
            print(f"Total words entered: {total_words}")
            print("Unique words:", sorted(unique_words))
            # Optionally, save the unique words to a file
            with open("unique_words.txt", "w") as file:
                file.write("\n".join(sorted(unique_words)))
            break
        else:
            # Add the word to the set of unique words
            unique_words.add(word_lower)
            total_words += 1

if __name__ == "__main__":
    main()
