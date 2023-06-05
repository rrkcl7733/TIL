for _ in range(int(input())):
    x = {}
    for i in input().split():
        x[i[0]] = x.get(i[0], 0) + 1
    print(max(x.values()))
