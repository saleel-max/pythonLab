# Function to calculate area of a square
def area_square(side):
    return side * side

# Function to calculate area of a rectangle
def area_rectangle(length, width):
    return length * width

# Function to calculate area of a triangle
def area_triangle(base, height):
    return 0.5 * base * height

# Ask user which shape
shape = input("Enter the shape (square/rectangle/triangle): ").lower()

if shape == "square":
    side = float(input("Enter the side of the square: "))
    print("Area of the square:", area_square(side))

elif shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print("Area of the rectangle:", area_rectangle(length, width))

elif shape == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print("Area of the triangle:", area_triangle(base, height))

else:
    print("Invalid shape entered!")
