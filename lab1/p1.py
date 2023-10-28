import math


numbers = input("Enter numbers separated by spaces: ").split()

# Convert input strings to integers
numbers = [int(num) for num in numbers]

# GCD using math.gcd
result = numbers[0]
for num in numbers[1:]:
    result = math.gcd(result, num)

print("The greatest common divisor is:", result)