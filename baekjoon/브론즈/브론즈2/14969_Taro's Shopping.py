def find_max_sum(n, m, prices):
    max_sum = -1
    for i in range(n):
        for j in range(i + 1, n):
            current_sum = prices[i] + prices[j]
            if m >= current_sum > max_sum:
                max_sum = current_sum
    return max_sum


while 1:
    n, m = map(int, input().split())
    if not n:
        exit()
    prices = list(map(int, input().split()))
    result = find_max_sum(n, m, prices)
    if result == -1:
        print('NONE')
    else:
        print(result)
