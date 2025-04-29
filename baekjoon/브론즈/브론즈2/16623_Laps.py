n, m = map(int, input().split())
readings = list(map(int, input().split()))

laps = 0
for i in range(1, m):
    if readings[i] < readings[i - 1]:
        laps += 1

print(laps)
