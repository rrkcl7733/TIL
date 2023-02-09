import math
import sys
input = sys.stdin.readline


while 1:
    n = int(input())
    if not n:
        exit()
    x, i = 0, 1
    while n:
        x += (n % 10) * math.factorial(i)
        n //= 10
        i += 1
    print(x)
