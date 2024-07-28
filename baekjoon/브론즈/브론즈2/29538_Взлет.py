M, N, a = map(int, input().split())
m = list(map(int, input().split()))

if a > 999:
    print("Impossible")
else:
    print((M + sum(m)) * a / (1000 - a))
