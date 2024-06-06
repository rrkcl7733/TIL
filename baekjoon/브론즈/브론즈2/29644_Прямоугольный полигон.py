S, P = map(int, input().split())
for i in range(300001):
    j = P // 2 - i
    if ((i + j) * 2, i * j) == (P, S):
        exit(print(j, i))
print(-1)
