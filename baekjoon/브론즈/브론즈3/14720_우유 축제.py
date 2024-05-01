input()
t = c = 0
for i in map(int, input().split()):
    if i == t:
        c += 1
        t = (t + 1) % 3
print(c)
