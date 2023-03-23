n = input()
c = 0
while len(n) != 1:
    t = 1
    for i in n:
        t *= int(i)
    c += 1
    n = str(t)
print(c)
