def stringld_simulation(words):
    steps = 0
    while 1:
        words = [word[1:] for word in words if word]

        if any(word == "" for word in words):
            break

        if len(set(words)) < len(words):
            break

        steps += 1
    print(steps)


while 1:
    n = int(input())
    if n < 1:
        exit()
    words = [input() for _ in range(n)]
    stringld_simulation(words)
