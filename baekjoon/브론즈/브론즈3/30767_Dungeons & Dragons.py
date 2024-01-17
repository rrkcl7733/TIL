n, a, b, c, d = [int(input()) for i in range(5)]

if a + c <= n <= b + d:
    x = max(n - d, a)
    y = min(n - c, b)
    print(y - x + 1)
else:
    print(0)
