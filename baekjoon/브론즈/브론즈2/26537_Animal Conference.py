from math import dist, inf
from itertools import combinations


for _ in range(int(input())):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    min_dist = inf
    p = q = None
    for a, b in combinations(sorted(mat), 2):
        d = dist(a, b)
        if d < min_dist or (d == min_dist and (a, b) < (p, q)):
            min_dist = d
            p, q = a, b
    print(*p, *q)
