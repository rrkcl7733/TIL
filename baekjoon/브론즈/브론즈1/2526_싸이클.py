n, p = map(int, input().split())
old = n
res = []

while 1:
    new = (n * old) % p

    if new in res:
        print(len(res) - res.index(new))
        exit(0)
    res.append(new)
    n = new
