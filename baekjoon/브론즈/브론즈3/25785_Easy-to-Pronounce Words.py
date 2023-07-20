a = input()
x = ('a', 'e', 'i', 'o', 'u')
for i in range(len(a) - 1):
  if a[i] not in x and a[i + 1] not in x:
    print(0)
    exit()
  elif a[i] in x and a[i + 1] in x:
    print(0)
    exit()
print(1)
