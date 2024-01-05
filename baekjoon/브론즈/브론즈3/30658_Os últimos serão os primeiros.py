while True:
    n = int(input())
    if n == 0:
        break

    teams = [int(input()) for _ in range(n)]
    teams.reverse()

    for team in teams:
        print(team)
    print(0)
