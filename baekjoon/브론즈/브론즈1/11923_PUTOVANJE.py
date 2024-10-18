N, C = map(int, input().split())
w = list(map(int, input().split()))

max_count = 0
for i in range(N):
    cost = count = 0
    for j in range(i, N):
        if cost + w[j] <= C:
            cost += w[j]
            count += 1
    max_count = max(max_count, count)

print(max_count)
