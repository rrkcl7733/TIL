N = int(input())
current = int(input())
total = 0

for _ in range(N):
    target = int(input())
    diff = abs(current - target)
    total += min(diff, 360 - diff)
    current = target

print(total)
