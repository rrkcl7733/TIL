import sys

input = sys.stdin.readline
scenario = 1
while 1:
    o, w = map(int, input().split())
    if o < 1:
        exit()

    dead = False
    while 1:
        cmd, n = input().split()

        if cmd == "#":
            break

        n = int(n)
        if not dead:
            if cmd == "E":
                w -= n
            elif cmd == "F":
                w += n

            if w <= 0:
                dead = True

    if dead:
        status = "RIP"
    elif o / 2 < w < 2 * o:
        status = ":-)"
    else:
        status = ":-("

    print(scenario, status)
    scenario += 1
