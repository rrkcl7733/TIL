t, d, m = map(int, input().split())
x = 0
for i in [int(input()) for _ in range(m)]:
    if i - x >= t:
        print('Y')
        exit()
    x = i
if (not x and t <= d) or (d - x >= t):
    print('Y')
else:
    print('N')
