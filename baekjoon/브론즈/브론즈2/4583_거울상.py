mirror = {
    'b': 'd', 'd': 'b',
    'p': 'q', 'q': 'p',
    'i': 'i', 'o': 'o',
    'v': 'v', 'w': 'w',
    'x': 'x'
}

while 1:
    word = input()
    if word == "#":
        exit()
    try:
        result = "".join(mirror[ch] for ch in reversed(word))
        print(result)
    except KeyError:
        print("INVALID")
