import sys


input = sys.stdin.readline
while True:
    n = int(input())
    if n < 1:
        break
    arr = list(map(int, input().split()))

    count = 0
    for i in range(n - 3):
        if arr[i:i + 4] == [2, 0, 2, 0]:
            count += 1
    print(count)
