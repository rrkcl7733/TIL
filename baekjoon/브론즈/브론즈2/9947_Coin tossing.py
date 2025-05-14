while 1:
    player1, player2 = input().split()
    if player1 == '#':
        exit()

    score1 = score2 = 0

    for _ in range(int(input())):
        call, result = input().split()
        if call == result:
            score1 += 1
        else:
            score2 += 1

    print(player1, score1, player2, score2)
