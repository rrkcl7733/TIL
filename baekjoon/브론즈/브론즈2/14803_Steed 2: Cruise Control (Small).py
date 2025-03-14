for t in range(int(input())):
    D, N = map(int, input().split())
    horses = [list(map(int, input().split())) for _ in range(N)]
    max_time = 0
    for horse in horses:
        K, S = horse
        time = (D - K) / S
        max_time = max(max_time, time)
    max_speed = D / max_time
    print(f'Case #{t + 1}: {max_speed}')
