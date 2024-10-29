t = input()
ans = 0
for _ in range(int(input())):
    a = input()
    a += a
    if t in a:
        ans += 1
print(ans)
