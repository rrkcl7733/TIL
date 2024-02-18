import math


n, s = map(int, input().split())
print(math.ceil(max(list(map(int, input().split()))) / 1000 * s))
