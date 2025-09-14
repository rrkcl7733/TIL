N = int(input())
nxt = {}
for _ in range(N - 1):
    S, D, C = map(int, input().split())
    nxt[S] = (D, C)

cur = 1
ans = 0

for _ in range(N - 1):
    D, C = nxt[cur]
    ans ^= C
    cur = D

print(ans)
