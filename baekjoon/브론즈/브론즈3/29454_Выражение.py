n = int(input())
a = list(map(int, input().split()))
t = sum(a)
for i in range(n):
    if t == 2 * a[i]:
        print(i + 1)
        break
