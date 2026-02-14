R, C = map(int, input().split())
A, B = map(int, input().split())

board = []
for i in range(R):
    row = []
    for j in range(C):
        if (i + j) % 2:
            row.append('.')
        else:
            row.append('X')
    board.append(row)


for i in range(R):
    for _ in range(A):
        line = ''
        for j in range(C):
            # 각 칸을 B번 반복
            line += board[i][j] * B
        print(line)
