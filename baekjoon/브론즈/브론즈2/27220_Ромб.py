n = int(input())
a = int(input())
b = int(input())
l = [n * ['.'] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a <= abs(i - n // 2) + abs(j - n // 2) <= b:
            l[i][j] = '*'
for i in l:
    print(*i, sep='')
