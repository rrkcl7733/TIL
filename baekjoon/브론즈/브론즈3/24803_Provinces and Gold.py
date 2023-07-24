g, s, c = map(int, input().split())
t = g * 3 + s * 2 + c
if t < 2:
  print('Copper')
  exit()
for i, j in [('Province', 8), ('Duchy', 5), ('Estate', 2)]:
  if t >= j:
    x = i
    break
for i, j in [('Gold', 6), ('Silver', 3), ('Copper', 0)]:
  if t >= j:
    y = i
    break
print(f'{x} or {y}')
