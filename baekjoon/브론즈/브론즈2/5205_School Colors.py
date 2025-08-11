import math

def euclidean(c1, c2):
    return math.sqrt(
        (c1[0] - c2[0]) ** 2 +
        (c1[1] - c2[1]) ** 2 +
        (c1[2] - c2[2]) ** 2
    )


for t in range(int(input())):
    n = int(input())
    colors = [tuple(map(int, input().split())) for _ in range(n)]

    max_contrast = -1
    pairs = []

    for i in range(n):
        for j in range(i + 1, n):
            contrast = euclidean(colors[i], colors[j])
            if contrast > max_contrast:
                max_contrast = contrast
                pairs = [(i + 1, j + 1)]
            elif math.isclose(contrast, max_contrast):
                pairs.append((i + 1, j + 1))

    pairs.sort()

    print(f"Data Set {t + 1}:")
    for i in pairs:
        print(*i)

