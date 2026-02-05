for _ in range(int(input())):
    pos, s = input().split()
    pos = int(pos)
    result = s[:pos-1] + s[pos:]
    print(result)
