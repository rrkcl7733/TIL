import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, a, b = query
        s = sum(arr[a-1:b])
        print(s)
        arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
    else:
        _, a, b, c, d = query
        s1 = sum(arr[a-1:b])
        s2 = sum(arr[c-1:d])
        print(s1 - s2)
