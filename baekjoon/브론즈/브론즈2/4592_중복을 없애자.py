import sys


for line in sys.stdin:
    nums = list(map(int, line.split()))
    if nums[0] < 1:
        exit()
        
    result = []
    prev = None
    for x in nums[1:]:
        if x != prev:
            result.append(x)
        prev = x

    print(*result, "$")
