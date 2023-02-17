for _ in range(int(input())):
    x = 0
    a = input()
    for i in a:
        x += int(i)
    a = (int(a) % 1000) * 10
    x += a
    if x // 10000:
        x = str(x)[::-1][:4][::-1]
    elif not x // 1000:
        x += 1000
    print(x)
