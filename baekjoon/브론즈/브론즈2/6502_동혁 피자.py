import math
import sys

t = 1
for line in sys.stdin:
    if line[0] == '0':
        exit()
    r, w, l = map(int, line.split())

    diagonal = math.sqrt(w**2 + l**2)
    if diagonal <= 2 * r:
        print(f'Pizza {t} fits on the table.')
    else:
        print(f'Pizza {t} does not fit on the table.')
    t += 1
