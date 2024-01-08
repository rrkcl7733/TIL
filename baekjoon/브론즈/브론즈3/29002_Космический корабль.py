n = int(input())
f = list(map(int, input().split()))
s = sum(f)
for i in f:
    if i == s - i:
        x = i
        f.remove(i)
        break
print(*f, x)
