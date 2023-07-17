a = input()
i = a.index('U')
for idx in range(len(a) - 1, i, -1):
    if a[idx] == 'F':
        j = idx
        break
x = '-' * i + 'U' + 'C' * (j - i - 1) + 'F' + '-' * (len(a) - j - 1)
print(x)
