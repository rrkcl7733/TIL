a = b = c = d = 0
for _ in range(int(input())):
    i, j, k = map(int, input().split())
    if i == 1:
        d += 1
    else:
        if j in (1, 2):
            a += 1
        elif j == 3:
            b += 1
        else:
            c += 1
print(a, b, c, d, sep='\n')
