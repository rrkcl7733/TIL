input()
x = [0] * 5
a = input()
for i, v in enumerate(['H', 'I', 'A', 'R', 'C']):
    x[i] += a.count(v)
print(min(x))
