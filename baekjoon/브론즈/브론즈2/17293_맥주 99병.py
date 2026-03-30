def bottles(n):
    def bottle_str(k):
        if k == 0:
            return 'no more bottles'
        elif k == 1:
            return '1 bottle'
        else:
            return f'{k} bottles'

    for k in range(n, 0, -1):
        print(f'{bottle_str(k)} of beer on the wall, {bottle_str(k)} of beer.')
        print(f'Take one down and pass it around, {bottle_str(k-1)} of beer on the wall.\n')

    print('No more bottles of beer on the wall, no more bottles of beer.')
    print(f'Go to the store and buy some more, {bottle_str(n)} of beer on the wall.')


bottles(int(input()))
