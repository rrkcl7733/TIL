o, a, k = map(int, input().split())

for i in range(1, 151):
  for j in range(1, 151):
    if i * a + j * k == o:
      print(1)
      exit()
print(0)
