n, m = map(int, input().split())
a = list(map(int, input().split()))
res = a[0] % m

for i in a[1:]:
    res *= i
    res %= m
print(res)
