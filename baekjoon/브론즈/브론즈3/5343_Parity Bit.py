for _ in range(int(input())):
    x = 0
    a = input()
    for i in range(0, len(a), 8):
        if (a[i:i+7].count('1') % 2 and a[i+7] == '0') or (not a[i:i+7].count('1') % 2 and a[i+7] == '1'):
            x += 1
    print(x)
