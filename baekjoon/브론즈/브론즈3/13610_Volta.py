import math


x, y = map(int, input().split())
print(math.ceil(y / (y - x)))
