n = int(input())
a = []
i = 1
for _ in range(n):
    t, s = map(int, input().split())
    a.append((t, s, i))
    i += 1
a.sort(key=lambda x: (-x[1], x[0]))
print(a[0][0] + (a[0][2] - 1) * 20 if a[0][1] == 1 or a[0][1] == 4 else 0)
