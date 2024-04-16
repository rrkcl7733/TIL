input()
P = int(input())
answer = 0

for M in map(int, input().split()):
    X = M ** P
    if X > 0:
        answer += X

print(answer)
