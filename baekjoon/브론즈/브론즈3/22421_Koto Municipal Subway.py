while 1:
    D, E = map(int, input().split())
    if not D:
        break

    min_diff = float('inf')
    for x in range(D + 1):
        y = D - x
        cost = (x ** 2 + y ** 2) ** .5
        diff = abs(cost - E)
        min_diff = min(min_diff, diff)
    print(min_diff)
