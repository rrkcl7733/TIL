all_cards = {f"{suit} {value}" for suit in "SBVK" for value in range(1, 14)}

for _ in range(51):
    card = input()
    all_cards.remove(card)

print(*all_cards)
