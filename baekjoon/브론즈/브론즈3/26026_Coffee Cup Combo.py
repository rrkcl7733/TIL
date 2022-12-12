n = int(input())
a = [0] * n
for i, x in enumerate(input()):
    if x == '1':
        a[i] = 1
        try:
            a[i + 1] = 1
            a[i + 2] = 1
        except:
            pass
print(a.count(1))
