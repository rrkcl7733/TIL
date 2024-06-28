import sys
input = sys.stdin.read
data = input().splitlines()

alpha_to_morse = {}
index = 0
for i in range(26):
    alpha, morse = data[index].split()
    alpha_to_morse[alpha] = morse
    index += 1

W = int(data[index])
index += 1

morses = {}
for _ in range(W):
    word = data[index]
    morse = ''.join(alpha_to_morse[char] for char in word)
    morses[morse] = word
    index += 1

while index < len(data):
    W = int(data[index])
    index += 1
    if W == 0:
        break

    result = []
    OOV = False
    for _ in range(W):
        word = data[index]
        index += 1
        if OOV:
            continue
        if word in morses:
            if result:
                result.append(' ')
            result.append(morses[word])
        else:
            result = [word]
            OOV = True

    if OOV:
        print(f"{result[0]} not in dictionary.")
    else:
        print(''.join(result))
