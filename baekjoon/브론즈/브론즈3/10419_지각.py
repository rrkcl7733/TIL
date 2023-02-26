for _ in range(int(input())):
    n = int(input())
    for i in range(1, 100):
        if i + i ** 2 > n:
            break
    print(i - 1)
