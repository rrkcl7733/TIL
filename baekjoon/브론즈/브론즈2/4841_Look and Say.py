for _ in range(int(input())):
    a = input()
    cnt, ans = 1, ''
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            cnt += 1
        else:
            ans += str(cnt)
            ans += a[i - 1]
            cnt = 1
    ans += str(cnt) + str(a[-1])
    print(ans)
