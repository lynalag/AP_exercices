def main():
    
    unique_words = set()
    total_words = 0

    while True:
        
        word = input("Enter a word: ").strip()

       
        word_lower = word.lower()

       
        if word_lower in unique_words:
            
            print(f"You typed in {len(unique_words)} unique words.")
            print(f"Total words entered: {total_words}")
            print("Unique words:", sorted(unique_words))
           
            with open("unique_words.txt", "w") as file:
                file.write("\n".join(sorted(unique_words)))
            break
        else:
            # Add the word to the set of unique words
            unique_words.add(word_lower)
            total_words += 1

if __name__ == "__main__":
    main()
