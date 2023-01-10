x = ''
a = input()
i = 0
while i < len(a):
    x = x + a[i]
    if i >= len(a):
        x = x + a[-1]
    i += ord(a[i]) - 64
print(x)
