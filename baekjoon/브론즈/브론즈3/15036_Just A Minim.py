N = int(input())
res = 0
for n in map(int, input().split()):
    res += 2 if n == 0 else 1/n
print(res)
