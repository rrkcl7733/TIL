ans = []
for _ in range(int(input())):
    s = list(input())
    for i in range(len(s)):
        c = s[i]
        if c == 'B':
            if i >= 1 and s[i - 1] == '-':
                s[i - 1] = 'D'
            if i >= 2 and s[i - 2] == '-':
                s[i - 2] = 'D'
        elif c == 'S':
            if i >= 1 and s[i - 1] == '-':
                s[i - 1] = 'D'
            if i + 1 != len(s) and s[i + 1] == '-':
                s[i + 1] = 'D'
    ans.append(s.count('-'))
print(*ans)
