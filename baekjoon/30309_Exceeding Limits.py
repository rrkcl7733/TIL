from heapq import *
import sys


input = sys.stdin.readline
n, m, t = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    x, y, l, v = map(int, input().split())
    g[x - 1].append((y - 1, l, v))
    g[y - 1].append((x - 1, l, v))


def dijkstra(vv):
    dist = [float("inf")] * n
    dist[0] = 0
    q = [(0, 0)]
    while q:
        t, x = heappop(q)
        if t > dist[x]:
            continue
        for y, l, v in g[x]:
            if t + l / (v + vv) < dist[y]:
                dist[y] = t + l / (v + vv)
                heappush(q, (dist[y], y))
    return dist[-1]


if dijkstra(0) <= t:
    print(0)
    exit()

l, h = 0, 10**18
while min(h - l, 1 - l / h) > 1e-6:
    m = (l + h) / 2
    if dijkstra(m) <= t:
        h = m
    else:
        l = m
print(l)
