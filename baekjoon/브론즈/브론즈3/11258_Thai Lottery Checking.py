a0, m0 = input().split()
a1, m1 = input().split()
a2, m2 = input().split()
a3, m3 = input().split()
a4, m4 = input().split()
a5, m5 = input().split()
while 1:
    x = input()
    if x == '-1':
        exit()
    m = 0
    if x == a0:
        m += int(m0)
    if x[:3] == a1:
        m += int(m1)
    if x[:3] == a2:
        m += int(m2)
    if x[3:] == a3:
        m += int(m3)
    if x[3:] == a4:
        m += int(m4)
    if x[4:] == a5:
        m += int(m5)
    print(m)
