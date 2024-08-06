import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
nums = sorted(list(map(int, input().split())))
start, end = 0, N - 1

res = 0
while start < end:
    if nums[start] + nums[end] == M:
        res += 1
        end -= 1
    elif nums[start] + nums[end] < M:
        start += 1
    else:
        end -= 1

print(res)
