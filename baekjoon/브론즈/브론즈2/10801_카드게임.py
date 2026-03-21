A_cards = list(map(int, input().split()))
B_cards = list(map(int, input().split()))

A_score = B_score = 0

for a, b in zip(A_cards, B_cards):
    if a > b:
        A_score += 1
    elif a < b:
        B_score += 1

if A_score > B_score:
    print("A")
elif A_score < B_score:
    print("B")
else:
    print("D")
