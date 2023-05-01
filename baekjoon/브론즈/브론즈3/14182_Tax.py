while 1:
    n = int(input())
    if not n:
        exit()
    print(n if n < 1000001 else int(n * .8) if n > 5000000 else int(n * .9))
