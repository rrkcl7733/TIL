import math


x = 0
for _ in range(int(input())):
    a = input().split()
    if a[0] == 'S':
        x = max(x, (4 / 3) * float(a[1]) ** 3 * math.pi)
    elif a[0] == 'L':
        x = max(x, float(a[1]) ** 2 * float(a[2]) * math.pi)
    else:
        x = max(x, (1 / 3) * float(a[1]) ** 2 * float(a[2]) * math.pi)
print(f'{x:.3f}')
