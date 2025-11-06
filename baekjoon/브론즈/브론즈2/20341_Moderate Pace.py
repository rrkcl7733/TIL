n = int(input())
k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []
for i in range(n):
    x, y, z = k[i], a[i], b[i]
    # 세 값의 중앙값
    ans.append(sorted((x, y, z))[1])

print(*ans)
