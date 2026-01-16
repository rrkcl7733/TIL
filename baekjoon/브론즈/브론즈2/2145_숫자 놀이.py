while 1:
    n = int(input())
    if n < 1:
        exit()

    print(n % 9 if n % 9 else 9)
