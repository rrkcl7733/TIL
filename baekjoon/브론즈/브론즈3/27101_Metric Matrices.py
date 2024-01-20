n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
t = 5
for i in range(n):
    for j in range(n):
        if i == j and matrix[i][j] != 0:
            t = min(t, 1)
        if i != j and matrix[i][j] <= 0:
            t = min(t, 2)
        if matrix[i][j] != matrix[j][i]:
            t = min(t, 3)
        for k in range(n):
            if matrix[i][j] + matrix[j][k] < matrix[i][k]:
                t = min(t, 4)
print(t if t < 5 else 0)
