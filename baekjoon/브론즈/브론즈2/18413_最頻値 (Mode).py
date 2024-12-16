input()
a = list(map(int, input().split()))
print(max(map(a.count, a)))
