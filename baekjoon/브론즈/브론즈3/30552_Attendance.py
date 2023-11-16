x = ''
t = 1
for _ in range(int(input())):
  a = input()
  if not x:
    if a != 'Present!':
      x = a
  else:
    if a != 'Present!':
      print(x)
      t = 0
      x = a
    else:
      x = ''
if x:
  print(x)
  t = 0
if t:
  print('No Absences')
