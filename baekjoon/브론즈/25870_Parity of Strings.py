x = set()
a = input()
for i in a:
    x.add(a.count(i) % 2)
print(2 if len(x) > 1 else 0 if 0 in x else 1)
