n = int(input())
arr, ans = [0, 1, 2], [0, 0, 0]

for _ in range(n):
    a, b, g = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
    ans[arr[g-1]] += 1

print(max(ans))
