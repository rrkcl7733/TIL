n = int(input())

for _ in range(n):
    s, *arr = list(map(int, input().split()))
    for i in range(s - 2):
        if arr[i + 1] != arr[i] + 1:
            print(i + 2)
            break
