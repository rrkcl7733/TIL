def is_valid_calorie(a, b, c, d):
    minb = b - 0.5 if b != 0 else b
    maxb = b + 0.5 if b != 0 else b
    minc = c - 0.5 if c != 0 else c
    maxc = c + 0.5 if c != 0 else c
    mind = d - 0.5 if d != 0 else d
    maxd = d + 0.5 if d != 0 else d

    min_cal = minb * 9 + minc * 4 + mind * 4
    max_cal = maxb * 9 + maxc * 4 + maxd * 4

    return min_cal <= a < max_cal


while 1:
    line = input().strip()
    if line == "0 0 0 0":
        exit()
    a, b, c, d = map(int, line.split())
    print("yes" if is_valid_calorie(a, b, c, d) else "no")
