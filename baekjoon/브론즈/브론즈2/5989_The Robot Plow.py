def count_plowed_squares(X, Y, instructions):
    field = [[0] * Y for _ in range(X)]

    for xll, yll, xur, yur in instructions:
        for x in range(xll - 1, xur):
            for y in range(yll - 1, yur):
                field[x][y] = 1

    return sum(sum(row) for row in field)

X, Y, I = map(int, input().split())
instructions = [tuple(map(int, input().split())) for _ in range(I)]

print(count_plowed_squares(X, Y, instructions))
