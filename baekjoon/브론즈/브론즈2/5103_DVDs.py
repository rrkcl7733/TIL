while 1:
    stock_code = input().strip()
    if stock_code == '#':
        exit()

    M, S = map(int, input().split())

    for _ in range(int(input())):
        transaction = input().split()
        action = transaction[0]
        amount = int(transaction[1])

        if action == 'S':
            S = max(0, S - amount)
        else:
            S = min(M, S + amount)

    print(f'{stock_code} {S}')
