while 1:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        exit()
    print('Never speak again.' if a + b == 13 else 'To the convention.' if a > b else 'Left beehind.' if b > a else 'Undecided.')
