import math

N, K = map(int, input().split())
cows = [tuple(map(int, input().split())) for _ in range(K)]

for S, T, R in cows:
    pages_per_cycle = S * T
    full_cycles = N // pages_per_cycle
    remaining_pages = N % pages_per_cycle

    time = full_cycles * (T + R)
    if remaining_pages > 0:
        time += math.ceil(remaining_pages / S)
    else:
        time -= R

    print(time)
