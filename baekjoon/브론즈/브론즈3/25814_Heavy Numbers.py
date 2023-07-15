a = input().split()
for i in range(2):
    t = 0
    for x in a[i]:
        t += int(x)
    a[i] = len(a[i]) * t
print(1 if a[0] > a[1] else 2 if a[1] > a[0] else 0)
