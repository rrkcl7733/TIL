N, K = map(int, input().split())
q = [i for i in range(1, N+1)]
result = []
idx = 0

for i in range(N):
    idx = (idx + K - 1) % len(q)
    result.append(q.pop(idx))

print("<", end="")
print(*result, sep=', ', end='')
print(">")
