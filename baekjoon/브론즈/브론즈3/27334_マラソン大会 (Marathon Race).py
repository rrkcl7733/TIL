n = int(input())
a = list(map(int, input().split()))
x, c, v = [0] * n, 1, 1e9
while min(a) != 1e9:
    t = 0
    for _ in range(a.count(min(a))):
        x[a.index(min(a))] = c
        a[a.index(min(a))] = 1e9
        t += 1
    c += 1 * t
print(*x, sep='\n')
