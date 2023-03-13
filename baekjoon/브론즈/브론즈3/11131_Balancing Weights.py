for _ in range(int(input())):
    n = int(input())
    x = y = 0
    for i in map(int, input().split()):
        if i > 0:
            x += i
        else:
            y -= i
    print('Right' if x > y else 'Left' if x < y else 'Equilibrium')
