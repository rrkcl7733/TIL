input()
ans, x = 0, 1
for i in input():
    if i == 'L':
        if x != 1:
            x -= 1
    else:
        if x == 1:
            x += 1
        elif x == 2:
            x += 1
            ans += 1
        else:
            ans += 1
print(ans)
