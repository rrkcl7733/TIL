nums = [int(input()) for _ in range(int(input()))]
total = sum(nums)

for x in nums:
    if x * 2 == total:
        print(x)
        break
else:
    print("BAD")
