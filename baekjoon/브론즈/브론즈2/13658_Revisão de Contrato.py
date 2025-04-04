while 1:
    D, N = input().split()
    if D == '0':
        exit()
    ans = N.replace(D, '')
    print(int(ans) if ans != '' else 0)
