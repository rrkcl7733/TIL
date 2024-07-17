N = input()

if int(N) % 7 and '7' not in N:
    print(0)
elif not int(N) % 7 and '7' not in N:
    print(1)
elif int(N) % 7 and '7' in N:
    print(2)
else:
    print(3)
