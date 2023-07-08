m, e = [0] * 2, [0] * 2
for _ in range(int(input())):
    t, a, b = map(int, input().split())
    e[0] += a
    e[1] += b
    if a > b: m[0] += t
    else: m[1] += t
print(1 if e[0] > e[1] and m[0] > m[1] else 2 if e[1] > e[0] and m[1] > m[0] else 0)
