def can_form_palindrome(s):
    for i in range(len(s)):
        temp = s[:i] + s[i + 1:]
        if temp == temp[::-1]:
            return temp
    return 'not possible'


while 1:
    line = input()
    if line == "#":
        exit()
    print(can_form_palindrome(line))
