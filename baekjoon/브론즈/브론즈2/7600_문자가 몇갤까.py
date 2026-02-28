while 1:
    line = input()
    if line == "#":
        exit()
    letters = set()
    for ch in line:
        if ch.isalpha():
            letters.add(ch.lower())
    print(len(letters))
