

user_input = input("Enter numbers separated by commas: ")


numbers = [int(num.strip()) for num in user_input.split(',')]


odd_numbers = [num for num in numbers if num % 2 != 0]


print("Original list:", numbers)
print("List after removing even numbers:", odd_numbers)
