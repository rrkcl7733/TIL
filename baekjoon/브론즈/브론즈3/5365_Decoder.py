x = ''
input()
n = 1
for i in input().split():
    if len(i) >= n:
        x += i[n - 1]
    else:
        x += ' '
    n = len(i)
print(x)
