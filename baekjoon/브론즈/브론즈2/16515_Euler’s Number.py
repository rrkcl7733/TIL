import math


n = int(input())
e_approx = 1
for i in range(1, n + 1):
    e_approx += 1 / math.factorial(i)
print(e_approx)
