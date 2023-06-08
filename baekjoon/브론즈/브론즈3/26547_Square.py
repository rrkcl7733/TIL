for _ in range(int(input())):
    a = input()
    print(a)
    if len(a) == 1:
        continue
    i = 1
    while i < len(a) - 1:
        print(a[i] + ' ' * (len(a) - 2) + a[-(i + 1)])
        i += 1
    print(a[::-1])
