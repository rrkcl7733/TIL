import math


for _ in range(int(input())):
    a, b = map(int, input().split())
    g = math.gcd(a, b)
    l = a * b // g
    print(l, g)
