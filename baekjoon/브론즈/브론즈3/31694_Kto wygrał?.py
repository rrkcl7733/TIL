def solve():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    score_A, score_B = sum(A), sum(B)
    if score_A != score_B:
        return 'Algosia' if score_A > score_B else 'Bajtek'
    for i in range(10, -1, -1):
        if A.count(i) != B.count(i):
            return 'Algosia' if A.count(i) > B.count(i) else 'Bajtek'
    return 'remis'

print(solve())
