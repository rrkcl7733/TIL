from itertools import combinations


count = 0
for combination in combinations(map(int, input().split()), 3):
    a, b, c = sorted(combination)
    if a + b > c:
        count += 1

print(count)
