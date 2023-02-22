for _ in range(int(input())):
    a, b = map(float, input().split())
    x = (1 + 5 ** .5) / 2
    print('golden' if x - .01 <= a / b <= x + .01 else 'not')
