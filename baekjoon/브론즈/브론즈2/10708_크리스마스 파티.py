N = int(input())
M = int(input())
A = list(map(int, input().split()))

scores = [0] * (N + 1)

for i in range(M):
    guesses = list(map(int, input().split()))
    target = A[i]
    wrong_count = 0

    for j in range(1, N + 1):
        if guesses[j - 1] == target:
            scores[j] += 1
        else:
            wrong_count += 1

    scores[target] += wrong_count

for j in range(1, N + 1):
    print(scores[j])
