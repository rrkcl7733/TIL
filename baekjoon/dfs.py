def dfs(x, y):
    global house
    arr[x][y] = 0
    for di, dj in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
        ni, nj = x + di, y + dj
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1:
            house += 1
            dfs(ni, nj)





n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
cnt = 0
houses = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house = 1
            cnt += 1
            dfs(i, j)
            houses.append(house)
houses.sort()
print(cnt)
print(*houses, sep='\n')