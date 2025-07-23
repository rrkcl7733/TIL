n, m = map(int, input().split())
counts = [0] * m

for _ in range(n):
    votes = list(map(int, input().split()))
    for i, v in enumerate(votes):
        counts[i] += v

places = sorted([(-counts[i], i + 1) for i in range(m)])
print(*[place for _, place in places])
