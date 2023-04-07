for _ in range(int(input())):
    n = int(input())
    x = 0
    for i in range(1, int(n ** .5) + 1):
        if not n % i:
            x += 1
            if i ** 2 != n:
                x += 1
    print(n, x)
