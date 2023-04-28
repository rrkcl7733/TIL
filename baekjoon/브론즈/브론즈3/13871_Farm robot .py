n, m, idx = map(int, input().split())
a, i = [0] * n, 0
a[0] = 1
for x in map(int, input().split()):
    i += x
    i = n - 1 if i < 0 else 0 if i == n else i
    a[i] += 1
print(a[idx - 1])
