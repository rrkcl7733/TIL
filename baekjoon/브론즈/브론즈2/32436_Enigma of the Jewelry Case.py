import sys
input = sys.stdin.readline

N = int(input())
K = [list(map(int, input().split())) for _ in range(N)]

for i in range(4):

    for j in range(N):
        k1 = K[j]
        k2 = [K[n][j] for n in range(N)]
        if k1 != sorted(k1) or k2 != sorted(k2):
            break
    else:
        print(i)
        exit()
    K = [[K[i][j] for i in range(N)] for j in range(N)][::-1]
