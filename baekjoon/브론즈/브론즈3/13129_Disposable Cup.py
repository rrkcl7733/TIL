a, b, n = map(int, input().split())
print(*[(a + b) * n - i * b for i in range(n - 1, -1, -1)])
