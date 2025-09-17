def jumble_word(word):
    if len(word) <= 3:
        return word
    middle = word[1:-1]
    return word[0] + middle[::-1] + word[-1]


while 1:
    line = input()
    if line == "#":
        exit()
    jumbled = [jumble_word(word) for word in line.split()]
    print(*jumbled)
