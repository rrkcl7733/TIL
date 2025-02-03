n, m = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(m)]
l = list(range(n + 1))[1:]
for i in x:
    a, b = i
    l[a - 1] = b
print(*l, sep='\n')
