import sys
input = sys.stdin.readline


n, m = map(int, input().split())
x = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    x[a] += 1
    x[b] += 1
print(*x[1:], sep='\n')
