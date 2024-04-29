N = int(input())
ts = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for t in ts:
    if t[0] > -1:
        if (t[1] + t[2] == -2) or (t[0] <= t[1] and (t[2] < 0 or t[1] <= t[2])):
            cnt += 1

print(cnt)
