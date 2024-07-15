n, k = map(int, input().split())
n -= 1
k -= 1

if k:
    print(-1 if n % k else n // k)
else:
    print((not n) - 1)
