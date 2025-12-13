a, b, n, w = map(int, input().split())

solutions = []
for sheep in range(1, n):
    goat = n - sheep
    if a * sheep + b * goat == w:
        solutions.append((sheep, goat))

if len(solutions) == 1:
    print(solutions[0][0], solutions[0][1])
else:
    print(-1)
