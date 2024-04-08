n = int(input())
t = []
x = 0
for _ in range(n):
    a, b = map(int, input().split())
    if b:
        t.append(a)
for i in range(len(t) - 1):
    x = max(x, t[i + 1] - t[i])
print(x)
