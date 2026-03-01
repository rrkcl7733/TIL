n = int(input())
x = h = 0
while x <= n:
    x += 2 * h * h + 2 * h + 1
    h += 1
print(h - 1)
