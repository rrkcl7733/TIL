N, M = map(int, input().split())
t = N
while N:
    N //= M
    t += N
print(t)
