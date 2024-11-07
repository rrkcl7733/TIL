v = []
teacher = 0
for _ in range(int(input()) + 1):
    a, b = input().split()
    time = int(a[:2]) * 60 + int(a[3:])
    if b[0] == 't':
        teacher = time
    else:
        v.append(time)
s = input()
s = int(s[:2]) * 60 + int(s[3:])
print(len(list(filter(lambda x: x >= teacher and x >= s, v))))
