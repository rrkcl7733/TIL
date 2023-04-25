for _ in range(int(input())):
    a = list(map(int, input().split()))
    x = [0] * 9
    for i in range(2, a[0] * 2 + 1, 2):
        x[a[i]] += 1
    print(max(x))
