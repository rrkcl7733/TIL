for _ in range(int(input())):
    a, b, c = map(int, input().split())
    
    if c > a + 2 * b:
        print("NO")
    else:
        if c % 2 > a:
            print("NO")
        else:
            print("YES")
