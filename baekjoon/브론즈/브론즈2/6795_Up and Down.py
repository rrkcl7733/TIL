def calculate_distance(forward, backward, total_steps):
    cycle = forward + backward
    full_cycles = total_steps // cycle
    remaining_steps = total_steps % cycle

    # 거리 계산: 전체 주기 동안의 거리 + 남은 스텝 동안의 거리
    distance = full_cycles * (forward - backward)
    if remaining_steps <= forward:
        distance += remaining_steps
    else:
        distance += forward - (remaining_steps - forward)

    return distance


a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

nikky_distance = calculate_distance(a, b, s)
byron_distance = calculate_distance(c, d, s)

if nikky_distance > byron_distance:
    print('Nikky')
elif byron_distance > nikky_distance:
    print('Byron')
else:
    print('Tied')
