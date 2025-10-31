
user_input = input("Enter numbers separated by commas: ")

numbers = [int(num.strip()) for num in user_input.split(',')]

total = sum(numbers)

print("List:", numbers)
print("Sum of all items in the list:", total)
