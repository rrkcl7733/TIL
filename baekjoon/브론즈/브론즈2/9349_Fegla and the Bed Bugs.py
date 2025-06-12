for _ in range(int(input())):
    N, K = map(int, input().split())
    d = (N - K) // (K - 1)
    print(d)
