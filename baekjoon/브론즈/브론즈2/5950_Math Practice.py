A, B = map(int, input().split())
for E in range(A + 1, 63):
    s = str(1 << E)
    if int(s[0]) == B:
        print(E)
        exit()
print(0)
