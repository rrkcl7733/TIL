for _ in range(int(input())):
    n = int(input())
    sales = list(map(int, input().split()))
    total = 0
    for i in range(1, n):
        for j in range(i):
            if sales[j] <= sales[i]:
                total += 1
    print(total)
