def hailstone_max(h):
    max_val = h
    while h != 1:
        if h % 2 == 0:
            h //= 2
        else:
            h = 3 * h + 1
        if h > max_val:
            max_val = h
    return max_val


while 1:
    h = int(input())
    if h == 0:
        break
    print(hailstone_max(h))
