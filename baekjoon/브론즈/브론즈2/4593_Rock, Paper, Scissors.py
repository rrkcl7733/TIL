while 1:
    p1 = input()
    if p1 == 'E':
        exit()
    p2 = input()
    
    win_map = {'R': 'S', 'S': 'P', 'P': 'R'}
    p1_wins = 0
    p2_wins = 0

    for move1, move2 in zip(p1, p2):
        if move1 == move2:
            continue
        elif win_map[move1] == move2:
            p1_wins += 1
        else:
            p2_wins += 1

    print(f'P1: {p1_wins}')
    print(f'P2: {p2_wins}')
