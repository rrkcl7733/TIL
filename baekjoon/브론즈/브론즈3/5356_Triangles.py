for _ in range(int(input())):
    n, a = input().split()
    n, a = int(n), ord(a)
    for i in range(1, n + 1):
        print(chr(a) * i)
        a += 1
        if a == 91:
            a -= 26
    print()
