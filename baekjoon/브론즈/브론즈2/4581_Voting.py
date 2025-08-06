while 1:
    line = input()
    if line == "#":
        exit()

    absent = line.count('A')

    if absent >= len(line) / 2:
        print("need quorum")
    else:
        yes = line.count('Y')
        no = line.count('N')
        if yes > no:
            print("yes")
        elif no > yes:
            print("no")
        else:
            print("tie")
