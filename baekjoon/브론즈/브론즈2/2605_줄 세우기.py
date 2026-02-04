n = int(input())
nums = list(map(int, input().split()))

line = []

for i in range(n):
    student = i + 1
    k = nums[i]
    line.insert(len(line) - k, student)

print(*line)
