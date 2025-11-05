a = int(input())
b = int(input())
if (a - b) % 3 != 0:
    print(-1)
    exit()

y = a % 3
x = (a - y) // 3
z = (b - y) // 3

print(x, y, z)
