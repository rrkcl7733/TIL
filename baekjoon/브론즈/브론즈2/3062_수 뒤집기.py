for _ in range(int(input())):
    N = input()
    reversed_N = N[::-1]
    total = int(N) + int(reversed_N)
    if str(total) == str(total)[::-1]:
        print("YES")
    else:
        print("NO")
