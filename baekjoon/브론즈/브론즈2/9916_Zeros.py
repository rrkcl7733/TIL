import math

n = int(input())
factorial_value = math.factorial(n)

zero_count = str(factorial_value).count('0')
print(zero_count)
