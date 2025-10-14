while 1:
    n, m = map(int, input().split())
    if m < 1:
        exit()

    total_scores = [0] * n

    for _ in range(m):
        scores = list(map(int, input().split()))
        for i in range(n):
            total_scores[i] += scores[i]

    print(max(total_scores))
