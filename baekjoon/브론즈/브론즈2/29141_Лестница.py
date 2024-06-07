xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
a, b = map(int, input().split())

x, y = abs(xb - xa), abs(yb - ya)
ans = x // a
if not ans or ans * b < y:
    print(-1)
else:
    print(x, ans)
    print(y, ans)
