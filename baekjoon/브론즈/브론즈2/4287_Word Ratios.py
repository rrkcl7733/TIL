def get_diff(word1, word2):
    return [(ord(b) - ord(a)) % 26 for a, b in zip(word1, word2)]


def apply_diff(word, diff):
    result = []
    for c, d in zip(word, diff):
        new_char = chr((ord(c) - ord('a') + d) % 26 + ord('a'))
        result.append(new_char)
    return ''.join(result)


while 1:
    line = input()
    if line == '#':
        exit()
    word1, word2, word3 = line.split()
    diff = get_diff(word1, word2)
    word4 = apply_diff(word3, diff)
    print(word1, word2, word3, word4)
