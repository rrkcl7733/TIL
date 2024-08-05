while 1:
    key = input()
    if key == "0":
        break
    text = input()
    for i, c in enumerate(text):
        print(chr(65 + (ord(c) + ord(key[i % len(key)]) - 129) % 26), end='')

    print()
