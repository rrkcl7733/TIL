x, y = map(int, input().split())
if x < y:
    res = y + (x // 10) + x
else:
    res = x + (y // 10) + y
print(res)
