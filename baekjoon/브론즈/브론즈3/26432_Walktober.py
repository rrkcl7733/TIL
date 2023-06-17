for i in range(int(input())):
    n, m, p = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    a = list(map(list, zip(*a)))
    x = 0
    for t in a:
        x += max(t) - t[p - 1]
    print(f'Case #{i + 1}: {x}')
