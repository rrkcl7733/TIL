while 1:
    N = int(input())
    if N < 1:
        exit()

    joe = jean = jane = james = other = 0

    for _ in range(N):
        size = input()

        if size == 'M' or size == 'L':
            joe += 1
        elif size == 'S':
            james += 1
        elif size == 'X':
            other += 1
        else:
            if int(size) > 11:
                jean += 1
            else:
                jane += 1

    print(joe,jean,jane,james,other)
