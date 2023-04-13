x = [3] * 1001
t = set()
for i in range(1, 1001):
    for j in range(1, i):
        t.add(j/i)
    x[i] += len(t) * 2
for _ in range(int(input())):
    print(x[int(input())])
