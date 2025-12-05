c = [0] * 3
m = [0] * 3
data = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    c[i], m[i] = data[i][0], data[i][1]

order = [(0, 1), (1, 2), (2, 0)]

for i in range(100):
    src, dst = order[i % 3]
    move = min(m[src], c[dst] - m[dst])
    m[src] -= move
    m[dst] += move

print(*m, sep='\n')
