for _ in range(int(input())):
    a = list(map(int, input().split()))
    print(*a, end=' ')
    print('Check' if sum(a) != 180 else 'Seems OK')
