from math import ceil


for _ in range(int(input())):
    y, m, d = map(int, input().split())
    now = 0

    for i in range(1, y):
        now += 200
        if i % 3:
            now -= 5
    if y % 3:
        now += ceil((m - 1) / 2) * 20 + (m - 1) // 2 * 19 + d
    else:
        now += (m - 1) * 20 + d
    print(196471 - now)
