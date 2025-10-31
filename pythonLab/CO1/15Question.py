
color_list1 = input("Enter first list of colors (comma-separated): ")

color_list2 = input("Enter second list of colors (comma-separated): ")


list1 = [color.strip() for color in color_list1.split(",")]
list2 = [color.strip() for color in color_list2.split(",")]


result = [color for color in list1 if color not in list2]


print("Colors in first list not in second list:", result)
