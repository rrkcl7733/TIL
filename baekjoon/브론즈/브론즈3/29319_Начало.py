input()
a = sorted(list(map(int, input().split())))
print(sum(a) - a[-1])
