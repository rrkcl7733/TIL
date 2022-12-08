t = float(input())
x = 0
for _ in range(int(input())):
    a, b = map(float, input().split())
    x += t * (a * b)
print(x)
