import sys
input = sys.stdin.readline


for _ in range(int(input())):
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))
    found = 0
    for i in range(5):
        for j in range(5):
            if row1[i] == row2[j] and i != j:
                print('YES')
                found = 1
                break
        if found:
            break
    if not found:
        print('NO')
