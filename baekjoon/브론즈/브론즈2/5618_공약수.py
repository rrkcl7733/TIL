import math

n = int(input())
nums = list(map(int, input().split()))

g = nums[0]
for i in range(1, n):
    g = math.gcd(g, nums[i])

for i in range(1, g + 1):
    if not g % i:
        print(i)
