n = int(input())
x = 0    # 배터리
t = 0    # 직전 소모량
k = 0    # 기존 핸드폰
for i in list(map(int, input().split())):
    if k != i:
        x += 2
        t = 2
        k = i
    else:
        t *= 2
        x += t
    if x > 99:
        x = t = k = 0
print(x)
