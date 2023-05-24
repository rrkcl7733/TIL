n = int(input())
m = int(input())
x = min(n, m) * 2
if (n + m) % 2:
    x += 1
print(x)
