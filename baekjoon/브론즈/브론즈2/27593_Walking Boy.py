for _ in range(int(input())):
    N = int(input())
    t = list(map(int, input().split()))

    cnt = t[0] // 120
    for i in range(1, N):
        cnt += (t[i] - t[i - 1]) // 120
    cnt += (1440 - t[N - 1]) // 120

    print('NO' if cnt < 2 else 'YES')
