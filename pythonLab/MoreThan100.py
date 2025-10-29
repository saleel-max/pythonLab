nums = input("Enter a list of integers separated by spaces: ")
nums = [int(x) for x in nums.split()]
over_100 = [x for x in nums if x > 100]
print("Numbers over 100:", over_100)
