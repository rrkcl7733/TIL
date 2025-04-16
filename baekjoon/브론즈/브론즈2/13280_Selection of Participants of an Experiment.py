while 1:
    n = int(input())
    if n == 0:
        exit()

    scores = sorted(list(map(int, input().split())))
    min_diff = float('inf')
    
    for i in range(1, n):
        diff = scores[i] - scores[i - 1]
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
