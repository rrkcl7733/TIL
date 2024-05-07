r, c = map(int, input().split())
o = r
for _ in range(c - 1):
    o *= r - 1
print(o % 998244353)
