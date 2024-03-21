a = map(int, input().split())
m = 5000
for i in a:
    m -= [0, 500, 800, 1000][i]
print(m)
