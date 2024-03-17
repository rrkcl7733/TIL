n = int(input())

cnt = 0
for num in range(1, n + 1):
    for i in str(num):
        if i in ('3', '6', '9'):
            cnt += 1
print(cnt)
