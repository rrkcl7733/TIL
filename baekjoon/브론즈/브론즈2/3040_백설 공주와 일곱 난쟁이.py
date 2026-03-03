nums = [int(input()) for _ in range(9)]
total = sum(nums)

# 제외해야 할 두 난쟁이 찾기
for i in range(9):
    for j in range(i+1, 9):
        if total - (nums[i] + nums[j]) == 100:
            for n in range(9):
                if n not in (i, j):
                    print(nums[n])
            exit()
