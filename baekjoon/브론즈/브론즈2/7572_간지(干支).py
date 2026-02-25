branches = "ABCDEFGHIJKL"
# 기준점: 2013년은 F9
stem_base = 9   # 십간
branch_base = 5 # 십이지 (F)

diff = int(input()) - 2013

stem = (stem_base + diff) % 10
branch = (branch_base + diff) % 12

print(branches[branch] + str(stem))
