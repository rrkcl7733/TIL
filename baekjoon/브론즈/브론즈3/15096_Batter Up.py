input()
c = t = 0
for i in map(int, input().split()):
    if i > -1:
        t += i
        c += 1
print(t / c)
