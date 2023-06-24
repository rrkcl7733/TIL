n, m = map(int, input().split())
x = list(map(int, input().split())) + [0] * m
for i in range(n):
    for idx, v in enumerate(list(map(int, input().split()))):
        x[i] -= v
        x[idx] += v
print(*x)
