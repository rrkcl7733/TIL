n, k = map(int, input().split())
p = [-1] + list(int(input()) for _ in range(n - 1))
cs = [[] for _ in range(n + 1)]
costs = []
for u in range(n - 1, -1, -1):
    if len(cs[u]) == 0:
        cs[p[u]].append(1)
    else:
        cs[u].sort()
        costs += cs[u][:-1]
        cs[p[u]].append(cs[u][-1] + 1)
costs.append(cs[-1][0])
costs.sort(reverse=True)
while costs[-1] <= k:
    k -= costs[-1]
    costs.pop()
print(len(costs))
