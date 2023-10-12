n, k = map(int, input().split())
c = sum([int(input()) for _ in range(k)])
print((c + (-3) * (n - k)) / n, (c + 3 * (n - k)) / n)
