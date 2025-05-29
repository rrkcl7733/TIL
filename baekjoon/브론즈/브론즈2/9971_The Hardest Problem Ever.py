while 1:
    s = input()
    if s == 'START':
        decrypted = ''
        for char in input():
            if 'A' <= char <= 'Z':
                # 문자(ord(char))의 알파벳 인덱스를 구하고 5를 빼서 모듈러 연산 수행
                decrypted_char = chr((ord(char) - ord('A') - 5) % 26 + ord('A'))
                decrypted += decrypted_char
            else:
                decrypted += char
        print(decrypted)
    elif s == 'ENDOFINPUT':
        exit()
