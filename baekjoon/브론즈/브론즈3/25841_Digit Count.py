x = 0
a, b, c = map(int, input().split())
for i in range(a, b + 1):
    x += str(i).count(c)
print(x)
