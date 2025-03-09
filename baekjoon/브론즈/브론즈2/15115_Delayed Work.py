K, P, X = map(float, input().split())
min_cost = float('inf')

for i in range(1, 10001):
    temp = i * X + P * K / i
    min_cost = min(min_cost, temp)

print(f'{min_cost:.3f}')
