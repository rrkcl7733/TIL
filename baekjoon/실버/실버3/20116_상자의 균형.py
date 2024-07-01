n, l = map(int, input().split())
inp = list(map(int, input().split()))
s = 0
for i in range(n - 1, 0, -1):
    s += inp[i]
    if not (inp[i - 1] - l < s / (n - i) < inp[i - 1] + l):
        print('unstable')
        exit()

print('stable')
