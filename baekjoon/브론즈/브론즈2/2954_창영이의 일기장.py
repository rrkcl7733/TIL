vowels = set("aeiou")
i = 0
result = ''
s = input()
while i < len(s):
    ch = s[i]
    result += ch
    if ch in vowels:
        i += 3
    else:
        i += 1
print(result)
