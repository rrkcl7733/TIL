def total_coins(days):
    total = 0
    n = 1
    rem = days
    # 그룹별로 n일 동안 n개의 금화 지급
    while rem > 0:
        if rem >= n:
            total += n * n
            rem -= n
            n += 1
        else:
            total += n * rem
            break
    return total

while 1:
    d = int(input())
    if d < 1:
        exit()
    print(d, total_coins(d))
