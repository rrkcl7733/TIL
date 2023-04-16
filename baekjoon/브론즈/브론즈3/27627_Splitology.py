x = input()
for i in range(1, len(x)):
    a, b = x[:i], x[i:]
    if a == a[::-1] and b == b[::-1]:
        print(a, b)
        exit()
print('NO')
