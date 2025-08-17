import sys
input = sys.stdin.readline


for t in range((T := int(input()))):
    N = int(input())
    ranges = list(map(int, input().split()))
    cities = [int(input()) for _ in range(int(input()))]
    print(f"Case #{t + 1}: ", end='')
    result = []
    for city in cities:
        count = 0
        for i in range(0, 2*N, 2):
            if ranges[i] <= city <= ranges[i+1]:
                count += 1
        result.append(count)

    print(*result)
    input()
