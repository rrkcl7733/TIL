x = [0] * 26
a = b = 0
for i in input():
  x[ord(i) - 97] += 1
for i in x:
  if i:
    if i % 2:
      a += 1
    else:
      b += 1
print(1 if not b else 0 if not a else '0/1')
