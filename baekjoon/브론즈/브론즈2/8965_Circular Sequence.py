for _ in range(int(input())):
    s = input()
    n = len(s)
    # 가능한 모든 회전을 생성하여 최소 문자열 선택(사전순 비교)
    smallest = s
    for j in range(1, n):
        rotated = s[j:] + s[:j]
        if rotated < smallest:
            smallest = rotated
    print(smallest)
