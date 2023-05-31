x = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    x.append(a/b)
print(min(x), max(x), sum(x))
