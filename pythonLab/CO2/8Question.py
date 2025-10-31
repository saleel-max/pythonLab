
user_input = input("Enter words separated by spaces: ")


words = user_input.split()

if words:
    max_length = max(len(word) for word in words)
    print("Length of the longest word:", max_length)
else:
    print("No words entered.")
