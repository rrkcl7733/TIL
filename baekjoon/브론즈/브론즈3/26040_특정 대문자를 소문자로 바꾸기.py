a = input()
x = ''
d = input().split()
for i in a:
    if i in d:
        x += i.lower()
    else:
        x += i
print(x)
