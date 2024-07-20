N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]

leftUp = 0 # 왼쪽위 끝점의 위치
rightDown = 0 # 오른쪽 아래 끝점의 위치

for i in range(N):
    if leftUp:
        break
    for j in range(M):
        if arr[i][j] == "#":
            leftUp = (i, j)
            break

for i in range(N - 1, -1, -1):
    if rightDown:
        break
    for j in range(M - 1, -1, -1):
        if arr[i][j] == "#":
            rightDown = (i, j)
            break

# 중심의 위치
mid = ((leftUp[0] + rightDown[0]) // 2, (leftUp[1] + rightDown[1]) // 2)

if arr[leftUp[0]][mid[1]] == ".":
    print("UP")
elif arr[mid[0]][leftUp[1]] == ".":
    print("LEFT")
elif arr[mid[0]][rightDown[1]] == ".":
    print("RIGHT")
elif arr[rightDown[0]][mid[1]] == ".":
    print("DOWN")
