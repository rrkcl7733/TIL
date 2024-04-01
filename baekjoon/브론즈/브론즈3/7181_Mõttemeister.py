t = input()
N = int(input())
cnt = dict([(i, t.count(str(i))) for i in range(10)])

for _ in range(N):
    s = input()
    A = sum([min(cnt[i], s.count(str(i))) for i in range(10)])
    B = sum([t[i] == s[i] for i in range(4)])

    print(A, B)
