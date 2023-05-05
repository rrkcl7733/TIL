a, b = map(int, input().split())
x = 1
for i in range(a, b + 1):
    x *= i * (i + 1) // 2
print(x % 14579)
