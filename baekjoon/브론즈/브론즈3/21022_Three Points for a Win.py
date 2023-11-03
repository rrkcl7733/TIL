n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = 0
for i in range(n):
    if a[i] > b[i]:
        x += 3
    elif a[i] == b[i]:
        x += 1
print(x)
