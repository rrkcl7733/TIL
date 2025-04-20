J, R = map(int, input().split())
points = list(map(int, input().split()))

scores = [0] * J

for i in range(len(points)):
    player = i % J  # 현재 턴의 플레이어
    scores[player] += points[i]

max_score = max(scores)
winner = 0

for i in range(len(scores)):
    if scores[i] >= max_score:
        winner = i + 1

print(winner)
