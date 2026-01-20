while 1:
    d, m, y = map(int, input().split())
    if d < 1:
        exit()

    # 월별 일수
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    print(sum(days_in_month[:m - 1]) + d)
