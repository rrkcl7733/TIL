n = int(input())
x = [0] * 1001
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        x[i] += 1
print('gunilla has a point' if x.count(n) else 'edward is right')
