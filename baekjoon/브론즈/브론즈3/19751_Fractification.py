from itertools import permutations


p = list(map(int, input().split()))
m, x = 1e9, []
for l in list(permutations(p, 4)):
    a, b, c, d = l
    t = a / b + c / d
    if t < m:
        m = t
        x = l
print(*x)
