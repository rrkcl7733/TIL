A, B = map(int, input().split())
li = []
for i in range(-1000, 10001):
    if i * (2 * A - i) == B:
        li = list({-i, -(2 * A - i)})
        break
print(*sorted(li))
