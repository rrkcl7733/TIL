n = int(input())
x = 0
a = list(map(int, input().split()))
for i in range(n - 1):
    if a[i] < a[i + 1]:
        x += 1
print(x)
