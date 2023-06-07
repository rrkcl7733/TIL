for _ in range(int(input())):
    a, b, c = map(float, input().split())
    d = (b ** 2 - 4 * a * c) ** .5
    print(f'{round((-b + d) / (2 * a), 3):.3f}, {round((-b - d) / (2 * a), 3):.3f}')
