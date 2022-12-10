n, m = map(int, input().split())
x = 0
for _ in range(n):
    if not input().split().count('0'):
        x += 1
print(x)
