n = int(input())
x, y = map(int, input().split())
for _ in range(n - 1):
    di, d = input().split()
    d = int(d)
    if len(di) == 2: d /= 2 ** .5
    if 'N' in di: y += d
    if 'S' in di: y -= d
    if 'W' in di: x -= d
    if 'E' in di: x += d
print(x, y)
