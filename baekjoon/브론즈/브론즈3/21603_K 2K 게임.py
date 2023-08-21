n, k = map(int, input().split())
a = []
x, y = str(k)[-1], str(2 * k)[-1]
for i in range(1, n + 1):
    if str(i)[-1] not in (x, y):
        a.append(i)
print(len(a))
print(*a)
