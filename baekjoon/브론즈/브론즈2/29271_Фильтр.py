_, r, x = map(int, input().split())
a = list(map(int, input().split()))

current_oil = total_drained = 0

for ai in a:
    # 기름 붓기
    current_oil += ai
    # 필터 용량 초과 처리
    if current_oil > r:
        current_oil = r

    # 시스템으로 기름 흐름
    if current_oil <= x:
        total_drained += current_oil
        current_oil = 0
    else:
        total_drained += x
        current_oil -= x

print(total_drained)
