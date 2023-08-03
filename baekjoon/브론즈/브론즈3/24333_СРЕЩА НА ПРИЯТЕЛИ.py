a, b, c, d, k = map(int, input().split())
x = [0] * 50001
x[k] -= 1
for i in range(a, b + 1):
    x[i] += 1
for i in range(c, d + 1):
    x[i] += 1
print(x.count(2))
