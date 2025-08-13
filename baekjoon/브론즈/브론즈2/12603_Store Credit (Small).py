for t in range(int(input())):
    C = int(input())
    input()
    prices = list(map(int, input().split()))

    price_map = {}
    for idx, price in enumerate(prices):
        complement = C - price
        if complement in price_map:
            first_index = price_map[complement] + 1
            second_index = idx + 1
            print(f"Case #{t + 1}: {min(first_index, second_index)} {max(first_index, second_index)}")
            break
        price_map[price] = idx
