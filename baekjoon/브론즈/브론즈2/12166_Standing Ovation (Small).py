for tc in range(int(input())):
    smax, audience = input().split()

    standing = 0
    added = 0

    for i, ch in enumerate(audience):
        num = int(ch)
        if standing < i:
            # 현재까지 일어난 사람 수가 i보다 모자라면 친구를 추가
            diff = i - standing
            added += diff
            standing += diff
        standing += num

    print(f"Case #{tc + 1}: {added}")
