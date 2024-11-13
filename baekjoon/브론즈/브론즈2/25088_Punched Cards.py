for t in range(int(input())):
    x, y = map(int, input().split())
    print(f'Case #{t + 1}:')
    print('..' + '+-' * (y - 1) + '+')
    print('..' + '|.' * (y - 1) + '|')
    for _ in range(x - 1):
        print('+-' * y + '+')
        print('|.' * y + '|')
    print('+-' * y + '+')
