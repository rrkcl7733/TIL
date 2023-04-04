a, b = map(int, input().split())
x = y = 0
tmp = 1e9
for _ in range(int(input())):
    p, q = map(int, input().split())
    t = abs(a - p) + abs(b - q)
    if t < tmp:
        tmp = t
        x, y = p, q
print(x, y)
