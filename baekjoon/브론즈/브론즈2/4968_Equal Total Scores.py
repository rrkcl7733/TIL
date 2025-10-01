def find_exchange(taro, hanako):
    sum_taro = sum(taro)
    sum_hanako = sum(hanako)
    diff = sum_taro - sum_hanako

    # 두 사람의 점수 차가 홀수면 절대 같아질 수 없음
    if diff % 2 != 0:
        return -1

    target_diff = diff // 2
    hanako_set = set(hanako)
    best_pair = None

    for a in taro:
        b = a - target_diff
        if b in hanako_set:
            if best_pair is None or a + b < best_pair[0] + best_pair[1]:
                best_pair = (a, b)

    return best_pair if best_pair else -1

while 1:
    n, m = map(int, input().split())
    if n < 1:
        exit()

    taro = [int(input()) for _ in range(n)]
    hanako = [int(input()) for _ in range(m)]

    result = find_exchange(taro, hanako)
    if result == -1:
        print(-1)
    else:
        print(*result)
