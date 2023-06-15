for _ in range(int(input())):
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    print('YES' if a == b and a[0] ** 2 + a[1] ** 2 == a[2] ** 2 else 'NO')
