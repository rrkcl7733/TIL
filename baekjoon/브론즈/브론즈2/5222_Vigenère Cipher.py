def vigenere_encrypt(keyword, plaintext):
    ciphertext = []
    keyword_length = len(keyword)

    for i, ch in enumerate(plaintext):
        key_ch = keyword[i % keyword_length]
        shift = ord(key_ch) - ord('A')
        plain_val = ord(ch) - ord('A')
        cipher_val = (plain_val + shift) % 26
        cipher_ch = chr(cipher_val + ord('A'))
        ciphertext.append(cipher_ch)

    return ''.join(ciphertext)


for _ in range(int(input())):
    keyword, plaintext = input().split()
    result = vigenere_encrypt(keyword, plaintext)
    print(f"Ciphertext: {result}")
