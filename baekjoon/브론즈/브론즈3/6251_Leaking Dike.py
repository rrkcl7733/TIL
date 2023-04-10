while 1:
    n = int(input())
    if not n:
        exit()
    x = 0
    t = list(map(int, input().split()))
    idx = int(input()) - 1
    for i in range(n):
        if idx >= i:
            if t[idx] >= t[i]:
                x += t[idx] - t[i] + 1
        else:
            if t[idx] < t[i]:
                break
            else:
                x += t[idx] -t[i] + 1
    print(x)
