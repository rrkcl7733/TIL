for _ in range(int(input())):
    input()
    a = input().split()
    b = input().split()
    x = 0
    for i in a:
        for j in b:
            if i == j:
                x += 1
    print(x)
