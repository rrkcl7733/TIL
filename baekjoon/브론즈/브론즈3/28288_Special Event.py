a = [0] * 5
for _ in range(int(input())):
    t = input()
    for i in range(5):
        if t[i] == 'Y':
            a[i] += 1
x = max(a)
t = []
for i in range(5):
    if a[i] == x:
        t.append(str(i + 1))
print(','.join(t))
