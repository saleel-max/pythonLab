list1 = [int(x) for x in input("Enter the first list of integers: ").split()]
list2 = [int(x) for x in input("Enter the second list of integers: ").split()]

# a) Check if lists are of the same length
if len(list1) == len(list2):
    print("The lists are of the same length.")
else:
    print("The lists are not of the same length.")

# b) Check if sums are equal
if sum(list1) == sum(list2):
    print("The sums of the lists are equal.")
else:
    print("The sums of the lists are not equal.")

# c) Check if any value occurs in both lists
common_values = [x for x in list1 if x in list2]
if common_values:
    print("Values occurring in both lists:", common_values)
else:
    print("No values occur in both lists.")
