for _ in range(int(input())):
    res = 1
    for i in range(1, int(input()) + 1):
        res *= i
        while res % 10 == 0:  # 끝자리 0 제거
            res //= 10
        res %= 100000  # 값이 너무 커지지 않도록 제한
    print(res % 10)
