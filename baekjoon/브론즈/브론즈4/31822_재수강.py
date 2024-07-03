a = input()[:5]
ans = 0
for i in range(int(input())):
    if input()[:5] == a:
        ans += 1
print(ans)
