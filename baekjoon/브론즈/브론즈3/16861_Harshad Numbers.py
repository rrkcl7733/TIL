n = int(input())
while 1:
    if not n % sum(map(int, list(str(n)))):
        print(n)
        exit()
    else:
        n += 1
