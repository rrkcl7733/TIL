n = int(input())
a = input()
c = n // 10
x = 0
for i in range(0, n, c):
    if a[i:i + c].count('T') == c:
        x += 1
print(x)
