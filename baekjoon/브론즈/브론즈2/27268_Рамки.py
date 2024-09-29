h, w, n = map(int, input().split())

frame = [['.'] * w for _ in range(h)]
for i in range(n):
    r1, c1, r2, c2 = map(int, input().split())
    letter = chr(ord('a') + i)
    for j in range(r1 - 1, r2):
        frame[j][c1 - 1] = letter
        frame[j][c2 - 1] = letter
    for j in range(c1 - 1, c2):
        frame[r1 - 1][j] = letter
        frame[r2 - 1][j] = letter

for i in range(h):
    print(''.join(frame[i]))
