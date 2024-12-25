while (s := input())[0] != '0':
    n, l, r = map(int, s.split())
    nums = [int(input()) for _ in range(n)]
    cnt = 0
    for year in range(l, r + 1):
        for i in range(n):
            if not year % nums[i]:
                cnt += 1 - (i & 1)
                break
        else:
            cnt += 1 - n & 1
    print(cnt)
