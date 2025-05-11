n, dominant = input().split()
cards = [input() for _ in range(4 * int(n))]

score_dominant = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
score_non_dominant = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}

total_points = 0
for card in cards:
    card_symbol = card[0]
    card_suit = card[1]
    
    if card_suit == dominant:
        total_points += score_dominant[card_symbol]
    else:
        total_points += score_non_dominant[card_symbol]

print(total_points)
