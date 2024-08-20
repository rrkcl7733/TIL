cnt = 0
for i in range(int(input())):
    nums = [*map(int, input().split())]
    s = sum(nums)
    if s > 2 * nums[i]:
        print('NO')
        exit()
    cnt += 2 * nums[i] > s

if cnt:
    print('YES')
    print(cnt)
else:
    print('NO')
