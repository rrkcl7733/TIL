n, t = map(int, input().split())
x = 0
for i in map(int, input().split()):
    t -= i
    if t < 0:
        print(x)
        exit()
    x += 1
print(x)
