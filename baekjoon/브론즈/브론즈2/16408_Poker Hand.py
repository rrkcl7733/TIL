hand = input().split()
ranks = [card[0] for card in hand]
rank_counts = {}

for rank in ranks:
    rank_counts[rank] = rank_counts.get(rank, 0) + 1

print(max(rank_counts.values()))
