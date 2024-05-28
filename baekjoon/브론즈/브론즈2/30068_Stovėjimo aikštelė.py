import sys
input = sys.stdin.readline

record = [0] * 1001

for _ in range(int(input())):
    T, N = map(int, input().split())

    if record[N]:
        print(N, T - record[N])
        record[N] = 0

    else:
        record[N] = T
