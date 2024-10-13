def check_win(board, x, y):
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
    for dx, dy in directions:
        count = 1
        for i in range(1, 5):
            nx, ny = x + dx * i, y + dy * i
            if 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 'X':
                count += 1
            else:
                break
        for i in range(1, 5):
            nx, ny = x - dx * i, y - dy * i
            if 0 <= nx < 10 and 0 <= ny < 10 and board[nx][ny] == 'X':
                count += 1
            else:
                break
        if count > 4:
            print(1)
            exit()


board = [list(input()) for _ in range(10)]
for i in range(10):
    for j in range(10):
        if board[i][j] == '.':
            board[i][j] = 'X'
            check_win(board, i, j)
            board[i][j] = '.'
print(0)
