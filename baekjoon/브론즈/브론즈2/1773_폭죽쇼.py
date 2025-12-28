N, C = map(int, input().split())
periods = set(int(input()) for _ in range(N))

seen = bytearray(C + 1)
for p in periods:
    for t in range(p, C + 1, p):
        seen[t] = 1

print(sum(seen[1:]))
