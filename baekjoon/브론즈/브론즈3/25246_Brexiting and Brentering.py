s = input()
i = -1
while 1:
    if s[i] in 'aeiou':
        print(s[:len(s)+1+i] + 'ntry')
        exit()
    i -= 1
