while 1:
    line = input()
    if line == "END":
        exit()
    count = 1
    prev = line
    while 1:
        curr = str(len(prev))
        if curr == prev:
            print(count)
            break
        prev = curr
        count += 1
