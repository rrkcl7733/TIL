n = int(input())
a = [int(input()) for _ in range(n)]
print('S' if max(a) == a[0] else 'N')
