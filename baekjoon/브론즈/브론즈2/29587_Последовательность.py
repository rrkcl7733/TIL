from itertools import pairwise

n = int(input())
a = map(int, input().split())
if all(p < q for p, q in pairwise(a)):
    print(0)
else:
    print(n)
    print(*range(1, n + 1))
