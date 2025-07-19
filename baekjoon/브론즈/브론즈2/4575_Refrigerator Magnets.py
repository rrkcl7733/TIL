while 1:
    line = input()
    if line == "END":
        exit()

    letters = [c for c in line if c != ' ']

    if len(letters) == len(set(letters)):
        print(line)
