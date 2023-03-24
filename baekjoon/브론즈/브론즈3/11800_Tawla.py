x = ('', 'Habb Yakk', 'Dobara', 'Dousa', 'Dorgy', 'Dabash', 'Dosh')
y = ('', 'Yakk', 'Doh', 'Seh', 'Ghar', 'Bang', 'Sheesh')
for i in range(int(input())):
  print(f'Case {i + 1}:', end=' ')
  a, b = map(int, input().split())
  a, b = max(a, b), min(a, b)
  if a == b:
    print(x[a])
  elif (a, b) == (6, 5):
    print(y[a], 'Beesh')
  else:
    print(y[a], y[b])
