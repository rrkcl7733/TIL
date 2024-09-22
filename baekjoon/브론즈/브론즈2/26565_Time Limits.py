for _ in range(int(input())):
    m, s = map(int, input().split())
    datasets = list(map(int, input().split()))
    print((max(datasets) * s + 999) // 1000)  # 밀리초를 초로 변환하고 올림
