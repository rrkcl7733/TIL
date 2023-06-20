a = [input().split() for _ in range(3)]
a.sort(key=lambda t: int(t[1]) % 100)
x = ''
for i in a:
    x += i[1][-2] + i[1][-1]
print(x)
a.sort(key=lambda t: -int(t[0]))
x = ''
for i in a:
    x += i[2][0]
print(x)
