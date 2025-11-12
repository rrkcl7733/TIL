n, *disliked = map(int, input().split())
disliked = set(disliked)
count = 0

for _ in range(int(input())):
    pizza = list(map(int, input().split()))
    toppings = set(pizza[1:])
    # 싫어하는 토핑이 하나도 없으면 주문 가능
    if disliked.isdisjoint(toppings):
        count += 1

print(count)
