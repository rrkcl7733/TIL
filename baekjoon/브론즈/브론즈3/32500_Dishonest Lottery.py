from collections import Counter

n = int(input())

x = []
for i in range(n * 10):
    x += input().split()

x = Counter(x)
r = sorted([i for i in x if int(x[i]) > n * 2], key=lambda k: int(k))

print(' '.join(r) if r else -1)
