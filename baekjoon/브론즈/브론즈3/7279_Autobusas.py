n, k = map(int, input().split())
x = 0
t = 0
for _ in range(n):
    a, b = map(int, input().split())
    x = x + a - b
    t = max(t, x)
print(max(t - k, 0))
