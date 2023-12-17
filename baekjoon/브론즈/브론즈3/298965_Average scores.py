import sys


input = sys.stdin.readline
N = int(input())
scores = {'M': 0, 'J': 0, 'count_M': 0, 'count_J': 0}

for _ in range(N):
    player, points = input().split()
    points = int(points)
    if player == 'M':
        scores['M'] += points
        scores['count_M'] += 1
    elif player == 'J':
        scores['J'] += points
        scores['count_J'] += 1
avg_M = scores['M'] / max(scores['count_M'], 1)
avg_J = scores['J'] / max(scores['count_J'], 1)

print('M' if avg_M > avg_J else 'J' if avg_J > avg_M else 'V')
