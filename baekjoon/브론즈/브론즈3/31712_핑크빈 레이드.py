a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
for i in range(1667):
    for c, d in a:
        if not i % c:
            n -= d
    if n < 1:
        print(i)
        exit()
