for _ in range(int(input())):
    N, M = map(int, input().split())
    print(-1 if 12 > N or M < 4 else 11 * M + 4)
