A, B, C = map(int, input().split())
trucks = [tuple(map(int, input().split())) for _ in range(3)]

total_cost = 0
for t in range(1, 101):
    count = 0
    for start, end in trucks:
        if start <= t < end:
            count += 1
    if count == 1:
        total_cost += A
    elif count == 2:
        total_cost += 2 * B
    elif count == 3:
        total_cost += 3 * C

print(total_cost)
