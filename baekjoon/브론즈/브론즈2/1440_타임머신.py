from itertools import permutations


parts = list(map(int, input().split(":")))
count = 0
for perm in permutations(parts, 3):
    h, m, s = perm
    if 0 < h < 13 and 0 <= m < 60 and 0 <= s < 60:
        count += 1

print(count)
