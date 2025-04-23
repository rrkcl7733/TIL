for _ in range(int(input())):
    s = input()
    count_R = s.count('R')
    count_L = s.count('L')
    count_U = s.count('U')
    count_D = s.count('D')
    count_unknown = s.count('?')

    x = count_R - count_L
    y = count_U - count_D

    min_x = x - count_unknown
    max_x = x + count_unknown
    min_y = y - count_unknown
    max_y = y + count_unknown

    print(min_x, min_y, max_x, max_y)
