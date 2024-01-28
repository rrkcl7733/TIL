def parse(x):
    m, s = map(int, x.split(":"))
    return 60 * m + s


n, c = map(int, input().split())
total = 0
for _ in range(n):
    total += parse(input())
total -= (n - 1) * c
h = total // 3600
m, s = divmod(total % 3600, 60)
print(f'{h:02d}:{m:02d}:{s:02d}')
