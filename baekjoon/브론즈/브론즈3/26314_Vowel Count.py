for _ in range(int(input())):
    a = input()
    c = 0
    print(a)
    for i in ['a', 'e', 'i', 'o', 'u']:
        c += a.count(i)
    print(1 if c > len(a) / 2 else 0)
