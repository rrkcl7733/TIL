n, m = map(int, input().split())
a = list(map(int, input().split()))
x = t = 0
ans = []
for i in range(n):
    if a[i] <= m - x:
        ans.append(t)
        x += a[i]
    else:
        x = a[i]
        t += 1
        ans.append(t)
print(*ans, sep='\n')
