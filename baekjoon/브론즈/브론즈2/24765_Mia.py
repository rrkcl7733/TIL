def score(dice):
    if sum(dice) == 3:
        return 100
    if dice[0] == dice[1]:
        return 90 + dice[0]
    return max(dice) * 10 + min(dice)


while 1:
    s0, s1, r0, r1 = map(int, input().split())
    if not s0:
        exit()

    player1_score = score([s0, s1])
    player2_score = score([r0, r1])

    if player1_score > player2_score:
        print('Player 1 wins.')
    elif player1_score < player2_score:
        print('Player 2 wins.')
    else:
        print('Tie.')
