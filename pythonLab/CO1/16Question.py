
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) >= 2 and len(str2) >= 2:

    new_str1 = str2[1] + str1[1:]
    new_str2 = str1[1] + str2[1:]
    

    result = new_str1 + " " + new_str2


    print("Result:", result)
else:
    print("Both strings must have at least two characters.")
