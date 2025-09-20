import math

N = int(input())
cows = [tuple(map(int, input().split())) for _ in range(N)]

max_dist = -1
best_pair = (0, 0)

for i in range(N):
    for j in range(i + 1, N):
        x1, y1 = cows[i]
        x2, y2 = cows[j]
        dist = math.hypot(x2 - x1, y2 - y1)  # sqrt((x2-x1)^2 + (y2-y1)^2)
        if dist > max_dist:
            max_dist = dist
            best_pair = (i + 1, j + 1)

print(*sorted(best_pair))
