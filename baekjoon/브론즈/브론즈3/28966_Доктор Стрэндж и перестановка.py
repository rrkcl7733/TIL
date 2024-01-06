n = int(input())
a = list(map(int, input().split()))
x = []
for i in range(n):
    if (not i % 2 and not a[i] % 2) or (i % 2 and a[i] % 2):
        x.append(i + 1)
    if len(x) > 2:
        print(-1, -1)
        exit()
if len(x) == 1:
    print(-1, -1)
elif not len(x):
    if n == 2:
        print(-1, -1)
    else:
        print(1, 3)
else:
    print(*x)
