n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = 0
for i in range(n):
    x += abs(a[i] - b[i])
print(x // 2)
