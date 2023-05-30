a = sorted([int(input()) for _ in range(4)])
print(1 if a[0] == a[3] or (a[1] == a[2] == a[3] and a[0] + int(input()) == a[1]) else 0)
