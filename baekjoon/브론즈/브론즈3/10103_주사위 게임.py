x = y = 100
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        y -= a
    elif b > a:
        x -= b
print(x)
print(y)
