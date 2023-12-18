n, m = map(int, input().split())
n += 10 * m
x = 0
for _ in range(5):
    a, b = map(int, input().split())
    x = max(x, a + 10 * b)
if n > x:
    print(0)
else:
    print(x - n + 1)
