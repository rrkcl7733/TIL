while 1:
    a = input().split()
    if a[0] == '#':
        exit()
    if int(a[1]) > 30 and (a[1] != '31' or int(a[2]) > 4 or int(a[3]) > 30):
        a[0], a[1] = '?', int(a[1]) - 30
    print(*a)
