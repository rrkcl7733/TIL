prices = list(map(int, input().split()))
coupons = list(map(int, input().split()))

if coupons[1] < coupons[2]:
    coupons[1], coupons[2] = coupons[2], coupons[1]

prices.sort(reverse=True)

price_total = sum(prices)
price_entire = (100 - coupons[0]) * sum(prices) / 100
price_each_item = ((100 - coupons[1]) * prices[0] + (100 - coupons[2]) * prices[1] + 100 * prices[2]) / 100

if price_entire < price_each_item:
    print(f'one {price_total - price_entire:.2f}')
else:
    print(f'two {price_total - price_each_item:.2f}')
