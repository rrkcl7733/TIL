x = dict()
for _ in range(int(input())):
    a, b = input().split()
    x[b] = a
n = input()
ans = ''
for i in range(0, len(n), 4):
    ans += x[n[i:i + 4]] if n[i:i + 4] in x.keys() else '?'
print(ans)
