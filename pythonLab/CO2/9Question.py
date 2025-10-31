
steps = int(input("Enter the number of steps for the top half: "))


for i in range(1, steps + 1):
    print("* " * i)


for i in range(steps - 1, 0, -1):
    print("* " * i)
