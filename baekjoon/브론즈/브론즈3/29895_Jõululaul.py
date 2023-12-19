n = int(input())
a = [0] * n
for i in range(n):
    a[i] = (i + 1) * (n - i)
print(*a, sep='\n')
