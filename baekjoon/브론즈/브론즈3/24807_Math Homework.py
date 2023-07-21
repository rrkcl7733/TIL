a, b, c, l = map(int, input().split())
x = []
for i in range(l // a + 1):
  for j in range(l // b + 1):
    for k in range(l // c + 1):
      if i * a + j * b + k * c == l:
        x.append((i, j, k))
if not x:
  print('impossible')
else:
  for i in x:
    print(*i)
