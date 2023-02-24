for _ in range(int(input())):
    x = y = 0
    for _ in range(9):
        a, b = map(int, input().split())
        x += a
        y += b
    print('Yonsei' if x > y else 'Korea' if y > x else 'Draw')
