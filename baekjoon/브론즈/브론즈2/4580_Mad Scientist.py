while 1:
    k, *P = list(map(int, input().split()))
    if k < 1:
        exit()
    prev = 0
    measurements = []

    for j in range(k):
        count = P[j] - prev
        measurements.extend([str(j + 1)] * count)
        prev = P[j]

    print(*measurements)
