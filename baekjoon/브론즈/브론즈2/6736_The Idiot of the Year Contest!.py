import math


for _ in range(int(input())):
    day, digit = map(int, input().split())

    factorial_result = str(math.factorial(day))
    count = factorial_result.count(str(digit))

    print(count)
