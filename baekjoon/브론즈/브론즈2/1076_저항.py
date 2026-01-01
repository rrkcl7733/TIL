# 색깔과 값 매핑
color_map = {
    "black": (0, 1),
    "brown": (1, 10),
    "red": (2, 100),
    "orange": (3, 1000),
    "yellow": (4, 10000),
    "green": (5, 100000),
    "blue": (6, 1000000),
    "violet": (7, 10000000),
    "grey": (8, 100000000),
    "white": (9, 1000000000)
}

c1 = input()
c2 = input()
c3 = input()

result = (color_map[c1][0] * 10 + color_map[c2][0]) * color_map[c3][1]

print(result)
