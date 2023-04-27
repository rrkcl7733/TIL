while 1:
    n = int(input())
    if not n:
        exit()
    print(n, end=' ')
    if n in (1916, 1940, 1944):
        print('Games cancelled')
    elif n > 1895 and not (n - 1896) % 4:
        print('Summer Olympics' if n < 2021 else 'No city yet chosen')
    else:
        print('No summer games')
