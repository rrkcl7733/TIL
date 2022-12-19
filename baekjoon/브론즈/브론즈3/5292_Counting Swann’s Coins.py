for i in range(1, int(input()) + 1):
    if not i % 15:
        print('DeadMan')
    elif not i % 3:
        print('Dead')
    elif not i % 5:
        print('Man')
    else:
        print(i, end=' ')
