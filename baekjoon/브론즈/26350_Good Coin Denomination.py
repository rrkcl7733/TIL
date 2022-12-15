for _ in range(int(input())):
    a = list(map(int, input().split()))
    print('Denominations: ', end='')
    print(*a[1:])
    for i in range(1, a[0]):
        if a[i] * 2 > a[i + 1]:
            print('Bad coin denominations!')
            break
    else:
        print('Good coin denominations!')
    print()
