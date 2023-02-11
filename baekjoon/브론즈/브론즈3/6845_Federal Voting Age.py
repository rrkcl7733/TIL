import datetime as dt


for _ in range(int(input())):
    a, b, c = map(int, input().split())
    day = dt.datetime(a, b, c)
    stand = dt.datetime(1989, 2, 27)
    print('Yes' if day <= stand else 'No')
