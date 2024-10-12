def isPalindrome(str, l, r, cnt):
    if l >= r:
        return [1, cnt]
    elif str[l] != str[r]:
        return [0, cnt]

    return isPalindrome(str, l + 1, r - 1, cnt + 1)


answer = []
for _ in range(int(input())):
    a = input()
    print(*isPalindrome(a, 0, len(a) - 1, 1))
