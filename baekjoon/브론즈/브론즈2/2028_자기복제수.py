for _ in range(int(input())):
    N = int(input())
    if str(N * N).endswith(str(N)):
        print("YES")
    else:
        print("NO")
