N, M = map(int, input().split())

min_sum, max_sum = 2, N + M
outcomes = []
max_count = 0

for s in range(min_sum, max_sum + 1):
    low = max(1, s - M)
    high = min(N, s - 1)
    count = 0
    if high >= low:
        count = high - low + 1
    outcomes.append((s, count))
    if count > max_count:
        max_count = count

for s, count in outcomes:
    if count == max_count:
        print(s)
