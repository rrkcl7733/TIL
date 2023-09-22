a, b = map(int, input().split())
if a - b > 0:
    x = 2 * b + 1
else:
    x = 2 * a - 1
print(x)
