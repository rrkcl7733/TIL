for _ in range(int(input())):
  x = [0, 0]
  for i in input():
    if i == 'a':
      x[0] += 1
    else:
      x[1] += 1
  print(min(x))
