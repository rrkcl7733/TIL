input()
x = t = 0
for i in map(int, input().split()):
    if i:
        t += 1
    else:
        x = max(x, t)
        t = 0
print(max(x, t))
