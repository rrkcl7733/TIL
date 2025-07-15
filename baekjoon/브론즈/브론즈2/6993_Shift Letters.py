for _ in range(int(input())):
    w, n_str = input().split()
    n = int(n_str)
    # 뒤에서 n글자를 잘라서 앞에 붙이기
    shifted = w[-n:] + w[:-n]
    print(f"Shifting {w} by {n} positions gives us: {shifted}")
