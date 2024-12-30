sequence = input()

res = [[1, 2], [3, 4]]

for s in sequence:
    if s == 'H':
        res[0], res[1] = res[1], res[0]
    else:
        res[0], res[1] = res[0][::-1], res[1][::-1]

for r in res:
    print(*r)
