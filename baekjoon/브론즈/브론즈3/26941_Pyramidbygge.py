n = int(input())
x, i = -1, 1
while 1:
    if n < 0:
        print(x)
        exit()
    n -= i ** 2
    i += 2
    x += 1
