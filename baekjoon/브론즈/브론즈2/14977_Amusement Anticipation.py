while 1:
    try:
        N = int(input())
        s = list(map(int, input().split()))
        if N < 3:
            print(1)
        else:
            N -= 1
            d = s[N] - s[N - 1]
            while N != 1 and s[N - 1] - s[N - 2] == d:
                N -= 1
            print(N)
    except:
        exit()
