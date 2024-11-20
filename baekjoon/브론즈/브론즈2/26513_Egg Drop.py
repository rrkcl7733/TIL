while 1:
    n, k = map(int, input().split())
    if not n:
        exit()
    drops = [input().split() for _ in range(n)]
    lowest_break = k
    highest_safe = 1

    for floor, result in drops:
        if result[0] == 'S':
            highest_safe = max(highest_safe, int(floor))
        else:
            lowest_break = min(lowest_break, int(floor))

    print(highest_safe + 1, lowest_break - 1)
