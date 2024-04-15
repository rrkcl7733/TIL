matrix = [list(map(int, input().split())) for _ in range(4)]
sums = set()
for row in matrix:
    sums.add(sum(row))
for col in zip(*matrix):
    sums.add(sum(col))

if len(sums) == 1:
    print('magic')
else:
    print('not magic')
