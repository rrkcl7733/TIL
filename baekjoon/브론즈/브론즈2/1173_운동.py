N, m, M, T, R = map(int, input().split())

if m + T > M:
    print(-1)
    exit()

time = exercise = 0
pulse = m

while exercise < N:
    if pulse + T <= M:
        # 운동
        pulse += T
        exercise += 1
    else:
        # 휴식
        pulse = max(m, pulse - R)
    time += 1

print(time)
