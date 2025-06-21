for t in range(int(input())):
    n, P, Q = map(int, input().split())    
    eggs = sorted(list(map(int, input().split())))
    
    count = 0  # 끓일 달걀의 수
    total_weight = 0  # 담은 달걀의 총 무게
    
    for weight in eggs:
        # 더 담을 수 있는 달걀 수가 남아있고, 총 무게 제한을 초과하지 않으면
        if count < P and total_weight + weight <= Q:
            count += 1
            total_weight += weight
        else:
            break
    
    print(f'Case {t + 1}: {count}')
