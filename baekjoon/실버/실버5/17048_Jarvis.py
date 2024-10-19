N = int(input())
v = list(map(int, input().split()))
u = list(map(int, input().split()))
m = {}
w = []

for i in range(N):
    diff = u[i] - v[i]
    if diff not in m:
        w.append(diff)
    m[diff] = m.get(diff, 0) + 1

ans = 0

for diff in w:
    ans = max(ans, m[diff])

print(ans)
