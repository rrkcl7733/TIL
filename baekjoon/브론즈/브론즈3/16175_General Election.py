for _ in range(int(input())):
    N, M = map(int, input().split())
    votes = [0] * N

    for _ in range(M):
        for i, v in enumerate(map(int, input().split())):
            votes[i] += v

    print(votes.index(max(votes)) + 1)
