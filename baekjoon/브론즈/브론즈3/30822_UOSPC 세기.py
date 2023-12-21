a = ['u', 'o', 's', 'p', 'c']
x = [0] * 5
input()
for i in input():
   if i in a:
     x[a.index(i)] += 1
print(min(x))
