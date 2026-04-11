for _ in range(int(input())):
    game = input()
    if len(game) % 2:
        print(game[0::2] + game[1::2])
        print(game[1::2] + game[0::2])
    else:
        print(game[0::2])
        print(game[1::2])
