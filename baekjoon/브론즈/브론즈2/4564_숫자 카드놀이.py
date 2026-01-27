while 1:
    S = input()
    if S == "0":
        exit()

    result = [S]
    while len(S) > 1:
        product = 1
        for digit in S:
            product *= int(digit)
        result.append(str(product))
        S = str(product)

    print(*result)
