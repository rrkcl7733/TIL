s = input()
N = int(s[1:])
if s[0] == 'C' and N > 36:
    print(-1)
else:
    if N < 37:
        print(0 - N // -4, 1, 1 - N % 2 * 2)
    else:
        print(1 + (54 - N) // 2, 0, 1 - N % 2 * 2)
