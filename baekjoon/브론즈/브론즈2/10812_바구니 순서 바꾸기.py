N, M = map(int, input().split())
baskets = list(range(1, N + 1))

for _ in range(M):
    i, j, k = map(int, input().split())
    i -= 1
    j -= 1
    k -= 1
    left = baskets[i:k]
    right = baskets[k:j+1]
    baskets[i:j+1] = right + left

print(*baskets)
