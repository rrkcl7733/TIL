for _ in range(int(input())):
    x = ''
    a = input()
    x = x + a[0]
    for i in range(1, len(a)):
        if x[-1] != a[i]:
            x = x + a[i]
    print(x)
