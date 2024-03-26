C, K, P = map(int, input().split())
print(K * (C * (C + 1) // 2) + P * (C * (C + 1) * (2 * C + 1) // 6))
