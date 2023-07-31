n = int(input())
x = 0
for _ in range(n):
    a = int(input())
    b = int(input())
    if a * 5 - b * 3 > 40:
        x += 1
print(x, '' if x < n else '+', sep='')
