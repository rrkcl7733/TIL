n, a, b = map(int, input().split())
for _ in range(n):
    print('NO' if a ** 2 + b ** 2 < int(input()) ** 2 else 'YES')
