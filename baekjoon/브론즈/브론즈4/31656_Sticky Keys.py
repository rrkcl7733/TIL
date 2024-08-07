arr = input()
ans = arr[0]
for i in range(1, len(arr)):
    if arr[i-1] != arr[i]:
        ans += arr[i]
print(ans)
