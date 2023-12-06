n = int(input())
a = input()[0]
t = int(input())
if a == 'a':
  if t % 2:
    print(t)
  else:
    print(t - 1)
else:
  if not t % 2:
    print(t)
  else:
    if t == 1:
      print(2)
    else:
      print(t - 1)
