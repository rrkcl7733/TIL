n = int(input())
nums = [int(input()) for _ in range(n)]
missing = [str(i) for i in range(1, nums[-1] + 1) if i not in nums]
print('good job' if not len(missing) else '\n'.join(missing))
