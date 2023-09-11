while 1:
    if input() == '0':
        exit()
    a = [abs(i - 2023) for i in list(map(int, input().split()))]
    print(a.index(min(a)) + 1)
