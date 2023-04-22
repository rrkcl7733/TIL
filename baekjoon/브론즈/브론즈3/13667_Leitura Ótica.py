while 1:
    n = int(input())
    if not n:
        exit()
    for _ in range(n):
        a = list(map(int, input().split()))
        m = min(a)
        print('*' if a.count(m) > 1 or sorted(a)[1] < 128 or sorted(a)[0] > 127 else ['A', 'B', 'C', 'D', 'E'][a.index(m)])
