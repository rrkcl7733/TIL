n, t = map(float, input().split())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

m = float('inf')
M = -m

for i in range(int(n)):
    m = min(m, round((x[i] + v[i] * t), 4))
    M = max(M, round((x[i] - v[i] * t), 4))

print(1 if m >= M else 0)
