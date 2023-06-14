for i in map(int, input().split()):
    for x in range(i - 1):
        print(' ' * x + '*' + ' ' * ((i - x - 2) * 2 + 1) + '*')
    print(' ' * (i - 1) + '*')
