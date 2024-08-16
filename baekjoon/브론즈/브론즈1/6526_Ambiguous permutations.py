import sys
input = sys.stdin.readline

while 1:
    n = int(input())
    if not n:
        break
    answer = "ambiguous"

    num = list(map(int, input().split()))
    for i in range(n):
        if num[num[i]-1] != i+1:
            answer = "not " + answer
            break

    print(answer)
