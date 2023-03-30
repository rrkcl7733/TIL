import sys
input = sys.stdin.readline


h, m, s = map(int, input().split())
for _ in range(int(input())):
    a = list(map(int, input().split()))
    if a[0] == 3:
        print(h, m, s)
    elif a[0] == 1:
        s += a[1]
    else:
        s -= a[1]
    m, s = m + s // 60, s % 60
    h, m = h + m // 60, m % 60
    h %= 24
