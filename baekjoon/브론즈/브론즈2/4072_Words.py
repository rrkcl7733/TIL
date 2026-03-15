while 1:
    line = input()
    if line == "#":
        exit()
    words = line.split(" ")
    restored = [w[::-1] for w in words]
    print(*restored)
