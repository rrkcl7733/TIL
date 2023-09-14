n, m, k = map(int, input().split())
b = n - m * (k - 1) - 1
a = max(n - m * k, 0)
print(a, b)
