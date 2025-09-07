def decrypt_message(shift, message):
    decrypted = []
    for ch in message:
        if 'a' <= ch <= 'z':
            new_char = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            decrypted.append(new_char)
        else:
            decrypted.append(ch)
    return ''.join(decrypted)
    

while 1:
    day, month, year = map(int, input().split())
    if day < 1:
        break
    message = input()
    shift = (day + month + year) % 25 + 1
    print(decrypt_message(shift, message))
