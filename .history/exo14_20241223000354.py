
word = input("Word: ")


frame_width = 30


left_padding = (frame_width - len(word)) // 2
right_padding = frame_width - len(word) - left_padding

# Print the frame
print("*" * frame_width)  # Top border
print("*" + " " * left_padding + word + " " * right_padding + "*")  # Word in the center
print("*" * frame_width)  # Bottom border
