def get_group(two_digits):
    x = int(two_digits)
    if x == 0:
        x = 100
    return (x - 1) // 4 + 1


while 1:
    parts = list(map(float, input().split()))
    if not parts[0]:
        exit()

    V_str, N_str, M_str = parts
    V = float(V_str)
    N = int(N_str)
    M = int(M_str)

    # N, M을 4자리 이상의 문자열로 변환 (숫자가 4자리 미만이면 앞에 0을 채움)
    fN = str(N).zfill(4)
    fM = str(M).zfill(4)

    prize = 0.0
    if fN[-4:] == fM[-4:]:
        prize = V * 3000
    elif fN[-3:] == fM[-3:]:
        prize = V * 500
    elif fN[-2:] == fM[-2:]:
        prize = V * 50
    else:
        # 두 번호의 마지막 2자리가 같은 그룹에 속하는지 확인
        if get_group(fN[-2:]) == get_group(fM[-2:]):
            prize = V * 16

    print(f'{prize:.2f}')
