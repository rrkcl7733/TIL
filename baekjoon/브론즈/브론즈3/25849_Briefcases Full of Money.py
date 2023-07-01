t = c = 0
x = [1, 5, 10, 20, 50, 100]
for i, v in enumerate(list(map(int, input().split()))):
    if t < v * x[i] or (t == v * x[i] and c > v):
        t = v * x[i]
        c = v
        idx = i
print(x[idx])
