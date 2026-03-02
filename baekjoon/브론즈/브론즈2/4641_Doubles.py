while 1:
    nums = list(map(int, input().split()))[:-1]
    if len(nums) < 2:
        exit()
    
    s = set(nums)
    count = 0
    for x in nums:
        if 2*x in s:
            count += 1
    print(count)
