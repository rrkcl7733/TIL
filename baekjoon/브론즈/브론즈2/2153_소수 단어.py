def char_value(ch):
    if 'a' <= ch <= 'z':
        return ord(ch) - ord('a') + 1
    else:  # 대문자
        return ord(ch) - ord('A') + 27

def is_prime(n):
    if n == 1:  # 1도 소수
        return 1
    if n < 2:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1


total = sum(char_value(ch) for ch in input())

if is_prime(total):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
