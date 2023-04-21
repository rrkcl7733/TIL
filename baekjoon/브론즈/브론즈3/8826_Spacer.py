for _ in range(int(input())):
    input()
    a = b = 0
    for i in input():
        if i == 'N':
            a += 1
        elif i == 'S':
            a -= 1
        elif i == 'E':
            b += 1
        else:
            b -= 1
    print(abs(a) + abs(b))
