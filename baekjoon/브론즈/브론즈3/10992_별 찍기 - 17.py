n = int(input())
for i in range(n - 1):
    if not i:
        print(' ' * (n - 1) + '*')
    else:
        print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + '*')
print('*' * (2 * n - 1))
