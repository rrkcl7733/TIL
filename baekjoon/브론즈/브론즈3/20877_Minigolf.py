input()
x = 0
for i, j in enumerate(map(int, input().split())):
  j = min(j, 7)
  x += j - 3 if i % 2 else j - 2
print(x)
