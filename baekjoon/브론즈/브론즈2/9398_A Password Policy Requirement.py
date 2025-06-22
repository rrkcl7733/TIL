for _ in range(int(input())):
    s = input()
    n = len(s)
    min_length = float('inf')
    found = False
    
    for i in range(n):
        # 남은 길이가 6보다 작으면 더 이상 검사할 수 없음.
        if n - i < 6:
            break
        # j는 i부터 시작해 최소 길이 6까지 고려
        for j in range(i + 6, n + 1):
            sub = s[i:j]
            # 세 조건에 대한 플래그
            has_upper = False
            has_lower = False
            has_digit = False
            for c in sub:
                if c.isupper():
                    has_upper = True
                elif c.islower():
                    has_lower = True
                elif c.isdigit():
                    has_digit = True
                # 셋 모두 충족하면 중단
                if has_upper and has_lower and has_digit:
                    break
            if has_upper and has_lower and has_digit:
                if len(sub) < min_length:
                    min_length = len(sub)
                    found = True
                # 같은 시작점에서 더 긴 부분 문자열은 볼 필요 없으므로 break.
                break

    if found:
        print(min_length)
    else:
        print(0)
