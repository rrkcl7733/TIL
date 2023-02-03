n = int(input())
a = list(input())
for i in range(1, n):
    if a[i] == a[i - 1]:
        a[i] = a[i].upper()
        a[i - 1] = a[i - 1].upper()
print(''.join(a))
