events = []
for _ in range(int(input())):
    s, t, b = map(int, input().split())
    events.append((s, b))
    events.append((t, -b))

events.sort()

current = 0
max_buckets = 0
for _, change in events:
    current += change
    max_buckets = max(max_buckets, current)

print(max_buckets)
