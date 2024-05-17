def check(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'k':
                for dx, dy in (2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2):
                    if 0 <= i + dx < 5 and 0 <= j + dy < 5 and board[i + dx][j + dy] == 'k':
                        print('invalid')
                        return
    print('valid')


n = int(input())
for i in range(n):
    a = [list(input()) for _ in range(5)]
    check(a)
    if i != n - 1:
        input()
