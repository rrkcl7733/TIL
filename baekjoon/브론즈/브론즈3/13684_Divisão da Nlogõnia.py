while 1:
    n = int(input())
    if not n:
        exit()
    x, y = map(int, input().split())
    for _ in range(n):
        a, b = map(int, input().split())
        print('NE' if a > x and b > y else 'NO' if a < x and b > y else 'SO' if a < x and b < y else 'SE' if a > x and b < y else 'divisa')
