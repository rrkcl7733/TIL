nums = [*map(int, list(input()))]

x = y = 0
temp = 2 ** (len(nums))
for i in nums:
    temp //= 2
    if i == 1:
        x += temp
    elif i == 2:
        y += temp
    elif i == 3:
        x += temp
        y += temp
print(len(nums), x, y)
