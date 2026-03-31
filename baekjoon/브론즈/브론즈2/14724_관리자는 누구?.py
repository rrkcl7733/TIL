clubs = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]

input()
max_scores = []

for _ in range(9):
    max_scores.append(max(map(int, input().split())))

print(clubs[max_scores.index(max(max_scores))])
