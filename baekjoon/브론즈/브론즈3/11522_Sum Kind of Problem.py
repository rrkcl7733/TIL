for _ in range(int(input())):
    i, x = map(int, input().split())
    a = x ** 2
    print(i, sum(range(1, x + 1)), a, a + x)
