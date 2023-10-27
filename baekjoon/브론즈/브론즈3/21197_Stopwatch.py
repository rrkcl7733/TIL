n = int(input())
if n % 2:
  print('still running')
  exit()
x = t = 0
for i, j in enumerate([int(input()) for _ in range(n)]):
  if i % 2:
    t += j - x
  x = j
print(t)
