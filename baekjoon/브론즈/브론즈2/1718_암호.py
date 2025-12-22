plain = input()
key = input()
result = ''
key_len = len(key)

for i, ch in enumerate(plain):
    if ch == ' ':
        result += ' '
        continue

    # 평문 문자와 키 문자
    p = ord(ch) - ord('a') + 1
    k = ord(key[i % key_len]) - ord('a') + 1

    # 암호화: 평문 - 키
    c = p - k
    if c <= 0:
        c += 26

    result += chr(c - 1 + ord('a'))

print(result)
