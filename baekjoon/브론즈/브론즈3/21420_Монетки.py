n = int(input())
a = [int(input()) for _ in range(n)]
print(min(a.count(1), n - a.count(1)))
