import sys
import math

for line in sys.stdin:
    D, VF, VG = map(int, line.split())

    time_thief = 12 / VF

    # 해안경비대가 도둑을 따라잡는 데 걸리는 시간
    distance_guard = math.sqrt(D ** 2 + 12 ** 2)
    time_guard = distance_guard / VG

    if time_guard <= time_thief:
        print('S')
    else:
        print('N')
