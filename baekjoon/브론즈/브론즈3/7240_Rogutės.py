n, s = map(int, input().split())
x = 0
for i in range(n):
    x += int(input())
    if i < n - 1 and x > s:
        x -= 1
print(x)
