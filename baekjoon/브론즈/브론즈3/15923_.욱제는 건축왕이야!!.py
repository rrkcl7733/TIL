n = int(input())
ans = 0
x, y = map(int, input().split())
sx, sy = x, y
for i in range(n - 1):
    nx, ny = map(int, input().split())
    ans += abs(nx + ny - x - y)
    x, y = nx, ny
ans += abs(x + y - sx - sy)
print(ans)
