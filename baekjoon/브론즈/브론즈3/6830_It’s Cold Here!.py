x = []
while 1:
    a, b = input().split()
    x.append((int(b), a))
    if a == 'Waterloo':
        x.sort()
        print(x[0][1])
        exit()
