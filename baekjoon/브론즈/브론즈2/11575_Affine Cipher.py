for t in range(int(input())):
    a, b = map(int, input().split())
    text = list(input())
    for i in range(len(text)):
        num = (a * (ord(text[i]) - ord('A')) + b) % 26
        text[i] = chr(num + ord("A"))
    print(''.join(text))
