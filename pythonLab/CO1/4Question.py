from collections import Counter
text = input("Enter a line of text: ")
words = text.lower().split()
word_counts = Counter(words)

print("Word occurrences:")
for word, count in word_counts.items():
    print(f"{word}: {count}")
