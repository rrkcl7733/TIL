for i in range(1, int(input()) + 1):
    if not i % 77:
        print('Wiwat!')
    elif not i % 11:
        print('Super!')
    elif not i % 7:
        print('Hurra!')
    else:
        print(i)
