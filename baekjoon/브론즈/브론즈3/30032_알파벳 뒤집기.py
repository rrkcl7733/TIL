n, d = map(int, input().split())
a = [input() for _ in range(n)]
if d == 1:
  for i in a:
    for j in i:
      if j in ('d', 'q'):
        x = 'd' if j == 'q' else 'q'
      else:
        x = 'p' if j == 'b' else 'b'
      print(x, end='')
    print()
else:
  for i in a:
    for j in i:
      if j in ('d', 'b'):
        x = 'd' if j == 'b' else 'b'
      else:
        x = 'p' if j == 'q' else 'q'
      print(x, end='')
    print()
