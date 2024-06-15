t = [0] * 101
for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, b):
        t[i] += 1
k = int(input())
print(0 if max(t) > k else 1)
