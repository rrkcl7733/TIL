for _ in range(int(input())):
    x, y, z, x1, y1, z1 = map(int, input().split())
    print(z + z1 + abs(x - x1) + abs(y - y1))
