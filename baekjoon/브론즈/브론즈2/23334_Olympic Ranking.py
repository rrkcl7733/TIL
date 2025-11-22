countries = []

for _ in range(int(input())):
    g, s, b, *name = input().split()
    countries.append((*map(int, (g, s, b)), name))

best = max(countries, key=lambda x: (x[0], x[1], x[2]))
print(*best[3])
