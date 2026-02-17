for _ in range(int(input())):
    encrypted = input()
    rule = list(input())

    ans = ''
    for i in encrypted:
        if i == ' ':
            ans += i
        else:
            ans += rule[ord(i) - 65]
    print(ans)
    
