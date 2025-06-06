for _ in range(int(input())):
    # (왼쪽: 서쪽, 오른쪽: 동쪽)
    villages = list(map(int, input().split()))

    move = 0
    result_stack = []
    # villages 리스트를 스택처럼 사용 (pop()하면 오른쪽(동쪽)부터 꺼짐)
    while villages:
        current = villages.pop() + move
        if villages:  # 아직 처리할 마을이 남았다면
            # 현재 값이 짝수이면 0, 홀수이면 1을 남기고
            result_stack.append(0 if current % 2 == 0 else 1)
            move = current // 2
        else:
            # 마지막(서쪽) 마을에서는 전체 인원을 기록
            result_stack.append(current)

    # 결과 스택은 동쪽부터 서쪽 순으로 쌓였으므로 역순으로 출력하면 서쪽부터 동쪽 순이 됨
    print(*result_stack[::-1])
