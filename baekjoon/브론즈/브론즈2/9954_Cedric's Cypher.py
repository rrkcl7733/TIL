while 1:
    if (encrypted_text := input()) == '#':
        exit()
    # 마지막 글자가 암호화된 'A'이므로, 이를 통해 shift 값을 구함.
    shift = ord(encrypted_text[-1]) - ord('A')
    # 마지막 글자를 제외한 나머지 문자열에 대해 복호화 수행
    decrypted = []
    for ch in encrypted_text[:-1]:
        if 'A' <= ch <= 'Z':
            # 대문자: 알파벳 A를 기준으로 인덱스를 조정, shift를 빼고 26으로 모듈러 연산 후 복원
            original_index = (ord(ch) - ord('A') - shift) % 26
            decrypted.append(chr(original_index + ord('A')))
        elif 'a' <= ch <= 'z':
            # 소문자: 알파벳 a를 기준으로 동일한 방식으로 복호화
            original_index = (ord(ch) - ord('a') - shift) % 26
            decrypted.append(chr(original_index + ord('a')))
        else:
            decrypted.append(ch)
    print(''.join(decrypted))
