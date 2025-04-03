while 1:
    if (n := int(input())) == 0:
        exit()
    heights = list(map(int, input().split()))
    peaks = 0
    for i in range(n):
        prev = heights[i - 1]
        current = heights[i]
        next = heights[(i + 1) % n]
        if (current > prev and current > next) or (current < prev and current < next):
            peaks += 1
    print(peaks)
