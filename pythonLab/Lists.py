
user_input = input("Enter integers separated by spaces: ")


positive_integers = [int(num) for num in user_input.split() if int(num) > 0]

print("Positive integers:", positive_integers)


N = int(input("Enter a number N: "))

for i in range(2, N+1):
    if i**2 == 16:
        print(i**2)


word = input("Enter a word: ")
vowels = [char for char in word if char.lower() in 'aeiou']
print(vowels)


word = input("Enter a word: ")
ascii_values = [ord(char) for char in word]
print(ascii_values)
