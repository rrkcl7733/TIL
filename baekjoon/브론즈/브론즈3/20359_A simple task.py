import math, sys


n = int(input())
for i in range(1, sys.maxsize, 2):
    if float(math.log(n / i, 2)).is_integer():
        print(i, int(math.log(n / i, 2)))
        exit()
