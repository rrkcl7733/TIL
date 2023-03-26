for c in range(int(input())):
    x = 0
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i][0] - arr[j][0]) * (arr[i][1] - arr[j][1]) < 0:
                x += 1
    print(f'Case #{c + 1}: {x}')
