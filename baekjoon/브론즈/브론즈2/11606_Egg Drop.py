n, k = map(int, input().split())

max_safe = 1  # 1층은 SAFE
min_broken = k  # k층은 BROKEN

for _ in range(n):
    floor_str, result = input().split()
    f = int(floor_str)
    if result[0] == 'S':
        if f > max_safe:
            max_safe = f
    else:
        if f < min_broken:
            min_broken = f

print(max_safe + 1, min_broken - 1)
