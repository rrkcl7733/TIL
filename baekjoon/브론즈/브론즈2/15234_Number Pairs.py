def count_pairs_with_sum_k(arr, k):
    count = 0
    seen = set()

    for num in arr:
        target = k - num
        if target in seen:
            count += 1
        seen.add(num)

    print(count)


n, k = map(int, input().split())
arr = list(map(int, input().split()))
count_pairs_with_sum_k(arr, k)
