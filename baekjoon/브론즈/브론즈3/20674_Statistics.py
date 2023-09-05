x = 0
t1 = 1e9
for i in range(int(input())):
    t2 = int(input())
    if t2 > t1:
        x += t2 - t1
    else:
        t1 = t2
print(x)
