n = 100 - int(input())
for i in [25, 10, 5, 1]:
    print(n // i, end=' ')
    n %= i
