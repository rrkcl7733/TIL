C, K = map(int, input().split())
unit = 10 ** K
print(((C + unit // 2) // unit) * unit)
