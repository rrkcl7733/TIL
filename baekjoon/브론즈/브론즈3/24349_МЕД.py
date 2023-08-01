n, a, b, c = map(int, input().split())
x = 0
if n > 1:
    if a < c or b < c: x = (n - 1) * min(a, b)
    else: x = min(a, b) + (n - 2) * c
print(x // 100, x % 100)
