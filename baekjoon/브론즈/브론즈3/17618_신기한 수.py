N = int(input())
cnt = 0
for i in range(1, N + 1):
    t = sum([int(c) for c in str(i)])
    if not i % t:
        cnt += 1
print(cnt)
