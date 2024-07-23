cnt = {}

for _ in range(int(input())):
    for i in input():
        if i != ' ':
            cnt[i] = cnt.get(i, 0) + 1

for i, j in cnt.items():
    print(i, j)
