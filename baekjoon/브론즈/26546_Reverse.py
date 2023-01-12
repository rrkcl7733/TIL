for _ in range(int(input())):
    x, i, j = input().split()
    print(x[:int(i)], end='')
    try:
        print(x[int(j):])
    except:
        print()
