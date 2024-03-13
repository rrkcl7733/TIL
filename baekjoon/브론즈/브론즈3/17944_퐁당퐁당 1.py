n, t = map(int, input().split())

arr = [i for i in range(1, (n * 2) + 1)]
arr.extend([i for i in range((n * 2) - 1, 1, -1)])

print(arr[(t % ((n * 4) - 2)) - 1])
