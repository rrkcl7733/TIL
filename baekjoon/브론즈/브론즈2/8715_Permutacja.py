n = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num < 1 or num > n:
        print('NIE')
        exit()

if len(set(nums)) == n:
    print('TAK')
else:
    print('NIE')
