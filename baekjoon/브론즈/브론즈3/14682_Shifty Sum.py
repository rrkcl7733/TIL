n = int(input())
x = n
for i in range(1, int(input()) + 1):
  x += n * 10 ** i
print(x)
