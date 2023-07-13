a = [100, 100, 200, 200, 300, 300, 400, 400, 500]
x = 0
for i, v in enumerate(list(map(int, input().split()))):
    if v > a[i]:
        print('hacker')
        exit()
    x += v
print('draw' if x > 99 else 'none')
