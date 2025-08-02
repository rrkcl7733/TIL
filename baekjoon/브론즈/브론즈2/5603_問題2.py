def transform(s):
    result = ''
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        result += str(count) + s[i]
        i += 1
    return result


n = int(input())
s = input()

for _ in range(n):
    s = transform(s)

print(s)
