import math


n = int(input())
t = 1
a = b = 0
while n:
    x = math.ceil(n / 2)
    n -= x
    if t < 0:
        a += x
    else:
        b += x
    t *= -1
print(a, b)
