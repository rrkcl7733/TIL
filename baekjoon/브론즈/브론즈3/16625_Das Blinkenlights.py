import math


p, q, s = map(int, input().split())
print('no' if math.lcm(p, q) > s else 'yes')
