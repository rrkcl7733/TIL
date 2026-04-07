for _ in range(int(input())):
    max_price = -1
    best_player = ""

    for _ in range(int(input())):
        price, name = input().split()
        price = int(price)

        if price > max_price:
            max_price = price
            best_player = name

    print(best_player)
