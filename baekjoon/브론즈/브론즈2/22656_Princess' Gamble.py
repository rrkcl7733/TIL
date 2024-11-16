while 1:
    N, M, P = map(int, input().split())
    if not N:
        exit()
    votes = [int(input()) for _ in range(N)]
    total_bets = sum(votes) * 100
    deduction = total_bets * P // 100
    pool = total_bets - deduction
    winning_bets = votes[M - 1]
    if winning_bets:
        print(pool // winning_bets)
    else:
        print(0)
