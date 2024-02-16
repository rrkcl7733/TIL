n = int(input())
print(*(set(range(1, n + 1)) - set(map(int, input().split()))))
