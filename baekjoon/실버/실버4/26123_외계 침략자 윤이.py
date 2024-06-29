n, d = map(int, input().split())

count = [0] * 300001

height = list(map(int, input().split()))
for x in height: count[x] += 1
now = max(height)
answer = 0

for _ in range(d):
    if not now: break
    answer += count[now]
    count[now - 1] += count[now]
    now -= 1
print(answer)
